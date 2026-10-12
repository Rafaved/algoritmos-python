"""
Desafio 15: Conversor de Dias da Semana
Objetivo: Converter um número (1 a 7) no respectivo dia da semana em formato de texto.
Tratamento: Retornar "Dia inválido" caso o número esteja fora do intervalo estabelecido.
"""

numero = int(input("Digite um numero de 1 a 7: "))
dia = 0

if numero == 1:
    dia = "Domingo!!!"
elif numero == 2:
    dia = "Segunda!!!"
elif numero == 3:
    dia = "Terça!!!"
elif numero == 4:
    dia = "Quarta!!!"
elif numero == 5:
    dia = "Quinta!!!"
elif numero == 6:
    dia = "Sexta!!!"
elif numero == 7:
    dia = "Sabádo!!!"
else:
    dia = "Inválido!!!"

print(f"O número digitado é {dia}")