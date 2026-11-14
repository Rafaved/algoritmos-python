"""
Arquivo: 16_caixa_eletronico.py

Desafio 16: Simulador de Caixa Eletrônico (Dispenser de Notas)
Objetivo: Calcular a quantidade mínima de notas entregues em um saque.

Regras de Negócio:
1. O sistema deve receber do usuário o valor exato que ele deseja sacar.
2. As notas disponíveis no caixa são apenas: R$ 100, R$ 50, R$ 20 e R$ 10.
3. O sistema deve bloquear qualquer tentativa de saque com valores que não sejam múltiplos de 10 (exemplo: R$ 125, R$ 32, R$ 5 não são permitidos).
4. O algoritmo deve ser otimizado para entregar sempre a menor quantidade possível de cédulas.
5. A saída do programa deve listar exatamente quantas notas de cada valor foram entregues. 
   Exemplo de saída esperada para um saque de R$ 280:
   - 2x nota(s) de R$ 100
   - 1x nota(s) de R$ 50
   - 1x nota(s) de R$ 20
   - 1x nota(s) de R$ 10
"""
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
while True: 
   saque = int(input("As notas disponíveis no caixa são apenas: R$ 100, R$ 50, R$ 20 e R$ 10.\n Qual o valor que você deseja sacar em R$:\n "))
   if saque % 10 != 0:
      print("\nO saque Inválido!!! Tente novamente.\n")
   else:
      nota_100 = saque // 100
      saque = saque % 100
      nota_50 = saque // 50
      saque = saque % 50
      nota_20 = saque // 20
      saque = saque % 20
      nota_10 = saque // 10
      print(f"- {nota_100}x nota(s) de R$ 100\n- {nota_50}x nota(s) de R$ 50\n- {nota_20}x nota(s) de R$ 20\n- {nota_10}x nota(s) de R$ 10")
      break
      