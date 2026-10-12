"""
Desafio 16: Simulador de Caixa Eletrônico (Dispenser de Notas)
Objetivo: Calcular a quantidade mínima de notas entregues em um saque.
Regras de Negócio:
- Notas disponíveis: R$ 100, R$ 50, R$ 20 e R$ 10.
- Bloquear saques que não sejam múltiplos de 10 (ex: R$ 125).
- Exemplo de saída para R$ 280: 2x 100, 1x 50, 1x 20, 1x 10.
"""

valor_saque = int(input("Quanto você quer sacar: "))
resto = valor_saque

if valor_saque % 10 != 0:
    print("Valor inválido! Digite valores múltiplos de 10.")
else:
    nota_100 = valor_saque // 100
    resto = resto % 100
    nota_50 = resto // 50
    resto = resto % 50
    nota_20 = resto // 20
    resto = resto % 20
    nota_10 = resto // 10
    resto = resto % 10
    print(f"O saque de {valor_saque} em notas será? \n{nota_100} notas de 100\n{nota_50} notas de 50\n{nota_20} notas de 20\n{nota_10} notas de 10")
 