from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Lista de credenciais para testar
casos_de_teste = [
    {"usuario": "tomsmith", "senha": "SuperSecretPassword!", "esperado": True},
    {"usuario": "tomsmith", "senha": "senhaerrada", "esperado": False},
    {"usuario": "", "senha": "", "esperado": False},
    {"usuario": "usuarioinvalido", "senha": "123456", "esperado": False},
]

# Setup do navegador uma única vez
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

for caso in casos_de_teste:
    # Limpar e preencher campos
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(caso["usuario"])
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(caso["senha"])
    driver.find_element(By.TAG_NAME, "button").click()

    sleep(1)  # Espera curta para carregar resposta

    # Verificar se login foi bem-sucedido
    sucesso = "You logged into a secure area!" in driver.page_source

    if sucesso == caso["esperado"]:
        print(f"✅ Login {'bem-sucedido' if sucesso else 'falhou'} para: {caso['usuario']}")
    else:
        print(f"❌ ERRO: Resultado inesperado para: {caso['usuario']}")

    driver.get("https://the-internet.herokuapp.com/login")

# Finaliza o navegador após todos os testes
driver.quit()
