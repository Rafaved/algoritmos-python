"""
Desafio 13: Calculadora de IMC
Objetivo: Receber peso (kg) e altura (m), calcular o IMC e classificar a faixa.
Fórmula: Peso / (Altura * Altura)
Classificação: Abaixo do peso (< 18.5), Peso ideal (18.5 a 24.9), Sobrepeso (25 a 29.9) ou Obesidade (>= 30).
"""

print("Sistema para calcular o IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    (f"Seu imc é {imc:.2f}. Abaixo do peso!")
elif imc <= 24.9:
    print(f"Seu imc é {imc:.2f}. Peso ideal! ")
elif imc < 30:
    print(f"Seu imc é {imc:.2f}. Sobrepeso!")
else:
    print(f"Seu imc é {imc:.2f}. Obesidade")