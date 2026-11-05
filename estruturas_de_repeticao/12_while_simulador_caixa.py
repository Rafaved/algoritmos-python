"""
Arquivo: 12_while_simulador_caixa.py

Solicitação (Ticket): Controle de Caixa de Loja
Setor: Operações / Vendas

Requisitos da regra de negócio:
O sistema deve simular o fechamento de caixa de um dia de vendas.
1. O programa inicia com `total_vendas = 0`.
2. O loop `while True` deve pedir continuamente o valor de cada venda realizada.
3. Se o usuário digitar um valor menor ou igual a zero (ex: 0 ou -5), o sistema deve entender que as vendas do dia encerraram e deve interromper o laço (break).
4. Se o valor for válido (maior que zero), o programa adiciona o valor ao `total_vendas` e exibe o subtotal acumulado até o momento.
5. Ao encerrar o laço, imprima a mensagem final com o valor total consolidado das vendas do dia.
"""

total_vendas = 0

while True:
    venda = float(input("\nDigite o valor da venda, ou digite '0' para encerrar o dia:\n "))
    if venda <= 0:
        print(f"Encerrando o dia, o valor final ficou em R${total_vendas:.2f}")
        break
    else:
        total_vendas += venda
        print(f"O subtotal acumulado até agora está em R${total_vendas:.2f}")
        
