"""
Desafio 12: Login Simples
Objetivo: Validar credenciais de usuário.
Regras de Negócio:
- Credenciais corretas (admin / 12345) retornam "Acesso Concedido".
- Usuário correto mas senha errada retorna "Senha incorreta".
- Qualquer outro usuário retorna "Usuário não encontrado".
"""

registro = input("Registre sua conta: ")
senha_registo = input("Regisre sua senha: ")
login = input("confirme seu registro para logar: ")
senha = input("Confirme sua senha: ")

if login == registro and senha == senha_registo:
    print("Acesso Concedido")
elif login == registro and senha != senha_registo:
    print("Senha incorreta.")
else:
    print("Usuário não encontrado.")