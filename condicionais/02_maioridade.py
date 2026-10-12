"""
Desafio 02: Validação de Maioridade
Objetivo: Verificar a idade informada pelo usuário e retornar se ele é "Maior de idade" (18+) ou "Menor de idade".
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Você tem {idade}, então é maior de idade")
elif idade <= 0:
    print(f"A idade {idade}, que você colocou é inválida")
else:
    print(f"Você tem {idade}, então é maior de idade")


