"""
Arquivo: 11_while_validador_senha.py

Solicitação (Ticket): Criação de Validador de Senha Forte
Setor: Segurança da Informação

Requisitos da regra de negócio:
O sistema deve solicitar que o usuário crie uma senha. O loop só deve ser interrompido e a senha aceita se ela atender a DUAS condições obrigatórias:
1. Ter pelo menos 8 caracteres de tamanho.
2. Não pode ser igual à palavra "senha" (independente de letras maiúsculas ou minúsculas).

Se a senha não atender aos dois critérios simultaneamente, o sistema deve recusar, exibir uma mensagem genérica de "Senha fraca, tente novamente" e pedir uma nova senha.
"""

while True:
    senha = input("\nDigite uma senha, em que tenha no mínimo 8 caracteres, e que não seja a palavra 'senha': \n")
    quantidade = len(senha)
    if senha.lower() == "senha":
        print("\nEssa senha não é permitido digite outra!!!")
    elif quantidade <= 7:
        print("\nEssa senha não atinge a quantidade mínima de caracteres!!!")
    else:
        print("\nSua senha foi registada!!!")
        break