# Casos de Teste – Tela de Login

| ID   | Cenário                         | Entrada                           | Resultado Esperado                 |
|------|----------------------------------|-----------------------------------|------------------------------------|
| CT01 | Login com dados válidos         | Usuário: tomsmith / Senha: SuperSecretPassword! | Acesso autorizado         |
| CT02 | Senha incorreta                 | Usuário: tomsmith / Senha: senhaerrada        | Mensagem de erro          |
| CT03 | Campos em branco                | Usuário: (vazio) / Senha: (vazio)             | Mensagem de obrigatoriedade |
| CT04 | Usuário inválido                | Usuário: errado / Senha: SuperSecretPassword! | Mensagem de erro          |
