from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def testar_login(usuario, senha):
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(senha)
    driver.find_element(By.CLASS_NAME, "radius").click()
    
    time.sleep(2)
    if "You logged into a secure area!" in driver.page_source:
        print(f"✅ Login bem-sucedido para: {usuario}")
    else:
        print(f"❌ Falha no login para: {usuario}")

    driver.quit()

# Casos de teste
testar_login("tomsmith", "SuperSecretPassword!")            # Esperado: Sucesso
testar_login("tomsmith", "senhaerrada")                     # Esperado: Falha
testar_login("", "")                                        # Esperado: Falha
testar_login("usuarioinvalido", "SuperSecretPassword!")     # Esperado: Falha
