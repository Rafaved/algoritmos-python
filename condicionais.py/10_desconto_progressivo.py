"""
Desafio 10: Sistema de Descontos Progressivos
Objetivo: Calcular o valor final de uma compra aplicando descontos baseados no valor total.
Regras de Desconto:
- 20% para compras acima de R$ 500,00.
- 10% para compras entre R$ 200,00 e R$ 500,00.
- 5% para compras abaixo de R$ 200,00.
"""
compra = float(input("Digite o valor da compra, para aplicação dos descontos: "))
desconto = 0

if compra > 500:
    desconto = 0.20
elif compra >= 200:
    desconto = 0.10
else:
    desconto = 0.05

compra = compra * (1 - desconto)

print(f"O valor da compra com os descontos aplicados foi para {compra:.2f}")
    
