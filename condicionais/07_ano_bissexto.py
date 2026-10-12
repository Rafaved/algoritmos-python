"""
Desafio 07: Verificador de Ano Bissexto
Objetivo: Receber um ano e calcular se ele é bissexto.
Regra matemática: É bissexto se for divisível por 4 e não por 100, ou se for divisível por 400.
"""

ano = int(input("digiter um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"o ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é um ano bissexto")