"""
Desafio 09: Classificação de Atletas por Idade
Objetivo: Categorizar um usuário de acordo com a idade.
Regras:
- Infantil (5 a 11 anos)
- Juvenil (12 a 17 anos)
- Adulto (18 a 49 anos)
- Master (50 anos ou mais)
- Bloquear idades menores que 5 anos.
"""

idade = int(input("Digite sua idade: "))

if idade < 5:
    print("Você não pode participar!!")
elif idade <= 11:
    print("Infantil")
elif idade <= 17:
    print("Juvenil")
elif idade <= 49:
    print("Adulto")
else:
    print("Master")  