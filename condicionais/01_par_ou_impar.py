"""
Desafio 01: Par ou Ímpar
Objetivo: Receber um número inteiro do usuário e classificá-lo como Par ou Ímpar.
"""
numero = int(input("Digite um número para verificar se é par ou ímpar: "))

if numero % 2 == 0:
    print(f"o número {numero} é par!")
else:
    print(f"O número {numero} é impar!")
    