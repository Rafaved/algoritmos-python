"""
Desafio 18: Calculadora de Frete e Benefícios Prime
Objetivo: Calcular o valor total de uma compra em um e-commerce.
Regras de Negócio:
1. Frete Base: SE/S = R$ 15 | CO = R$ 20 | N/NE = R$ 30.
2. Frete grátis para compras > R$ 300 ou para assinantes Prime.
3. Desconto extra de 10% no subtotal para assinantes Prime que gastarem mais de R$ 500.
"""

compra = float(input("Qual foi o valor gasto na compra: "))
prime = input("Você é assinante prime? ").lower()                                                                                                                                             
total = 0


if prime == "sim" and compra > 500:
    total = compra - (compra * 0.10)
    print(f"O valor de {compra} com a assinatura prime, gastando acima de R$500,00, ficou R${total}")
else:
    if compra > 300 or prime == "sim":
        total = compra
        print(f"O valor total da compra é {compra}")    
    else:
        frete_base = int(input("qual o tipo do seu frete?\n1 para SE/S, 2 para CO, 3 para N/NE: "))
        if frete_base == 1:
            total = compra + 15
            print(f"Com o frete para a região SE/S, ficou no valor de {total}")
        elif frete_base == 2:
            total = compra + 20
            print(f"Com o frete para a região CO, ficou no valor de {total}")
        elif frete_base == 3:
            total = compra + 30
            print(f"Com o frete para a região N/NE, ficou no valor de {total}")
        else:
            print("Você digitou os dados errados verifique novamente.")
