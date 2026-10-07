"""
Desafio 04: Comparador de Números
Objetivo: Receber dois números inteiros e identificar qual é o maior, ou informar se os valores digitados são iguais.
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

if numero_1 > numero_2:
    print("O primeiro número é maior!!!")
elif numero_1 == numero_2:
    print("Os números não iguais, ou seja não tem maior.")
else:
    print("O número 2 é maior")