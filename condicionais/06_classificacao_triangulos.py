"""
Desafio 06: Classificação de Triângulos
Objetivo: Receber três números correspondentes aos lados de um triângulo.
Regras de Negócio:
1. Validar se formam um triângulo (a soma de dois lados deve ser maior que o terceiro).
2. Classificar como Equilátero (3 lados iguais), Isósceles (2 lados iguais) ou Escaleno (3 diferentes).
"""

lado_1 = int(input("Digite o primeiro lado: "))
lado_2 = int(input("Digite o segundo lado: "))
lado_3 = int(input("Digite o terceiro lado: "))
validacao = (lado_1 + lado_2 > lado_3) and (lado_2 + lado_3 > lado_1) and (lado_1 + lado_3 > lado_2)

if validacao:
    if lado_1 == lado_2 == lado_3:
        print("É um triângulo Equilátero")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("É um triângulo Isósceles")
    else:
        print("É um triângulo Escaleno")
else:
    print("Não forma um triângulo, digite e tente novamente")
        
