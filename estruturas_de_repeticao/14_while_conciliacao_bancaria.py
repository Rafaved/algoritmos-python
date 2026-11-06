"""
Arquivo: 14_while_conciliacao_bancaria.py

Solicitação (Ticket): Motor de Processamento de Transações Financeiras
Setor: Engenharia de Software / Meios de Pagamento

Requisitos da regra de negócio:
Simular o processamento em lote de transações bancárias da empresa.

1. Saldo inicial da conta: R$ 1.000,00.
2. Contadores e Acumuladores (iniciar antes do loop):
   - total_depositos (inicia em 0)
   - total_saques (inicia em 0)
   - transacoes_recusadas (inicia em 0)
3. O laço `while True` deve solicitar o tipo de operação:
   - "C" para Crédito (Entrada de dinheiro)
   - "D" para Débito (Saída de dinheiro)
   - "FIM" para encerrar o processamento
4. Regras de Entrada e Movimentação:
   - Se o usuário digitar "FIM", quebre o laço (break).
   - Se digitar qualquer coisa diferente de "C", "D" ou "FIM", imprima "Operação inválida!" e recomece o laço.
   - Para operações "C" ou "D", peça o valor da transação (float).
   - Se o valor digitado for menor ou igual a zero, exiba "Valor inválido" e recomece o laço.
5. Regras Financeiras:
   - Se for "D" (Débito) e o valor for maior que o saldo atual:
     * Não altere o saldo.
     * Some +1 no contador `transacoes_recusadas`.
     * Exiba a mensagem: "Transação recusada: Saldo insuficiente!"
   - Se for "D" (Débito) e o saldo for suficiente:
     * Subtraia o valor do saldo.
     * Some o valor ao `total_saques`.
   - Se for "C" (Crédito):
     * Adicione o valor ao saldo.
     * Some o valor ao `total_depositos`.
6. Ao encerrar ("FIM"), exiba o Extrato Consolidado formatado em R$:
   - Saldo Final
   - Total Depositado
   - Total Sacado
   - Quantidade de Transações Recusadas
"""

saldo_inicial = 1000
total_depositos = 0
total_saques = 0
transacoes_recusadas = 0

while True:
   operacao = input("\nDigite 'C' para creditar na conta\nDigite 'D' para debitar da conta\nOu digite 'FIM' para encerrar a operação!!!\n").upper()
   if operacao == "FIM":
      print(f"Saldo Final = {saldo_inicial:.2f}\nTotal Depositado = {total_depositos:.2f}\nTotal Sacado = {total_saques:.2f}\nQuantidade de Transações Recusadas = {transacoes_recusadas}")
      break
   if operacao not in ["C", "D", "FIM"]:
      print("Operação inválida!!!\n")
   else:
      valor_numero = float(input("Digite o valor da operação:\n"))
      if valor_numero <= 0:
         print("Valor inválido!!!\n")
      elif operacao == "D" and valor_numero > saldo_inicial:
         print("Transação recusada: Saldo insuficiente!!!")
         transacoes_recusadas +=1
         saldo_inicial = saldo_inicial
      elif operacao == "D" and valor_numero <= saldo_inicial:
         saldo_inicial -= valor_numero
         total_saques += valor_numero
      elif operacao == "C":
         saldo_inicial += valor_numero
         total_depositos += valor_numero
      
      