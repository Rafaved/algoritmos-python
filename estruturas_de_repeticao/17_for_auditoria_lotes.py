"""
Arquivo: 17_for_auditoria_lotes.py

Desafio 01 (Bloco 1 - FOR com range): Auditoria de Lotes de Pedidos
Objetivo: Percorrer um intervalo numérico de identificadores (IDs) de pedidos, classificar os registros por regra de divisibilidade e gerar um relatório consolidado.

Regras de Negócio:
1. O sistema deve receber dois números inteiros do usuário: o ID inicial e o ID final do lote.
2. Caso o ID inicial seja maior que o ID final, o sistema deve exibir uma mensagem de erro ("Intervalo inválido!") e encerrar sem processar.
3. O intervalo deve ser inclusivo (ou seja, tanto o ID inicial quanto o ID final precisam entrar na verificação).
4. Para cada ID dentro do intervalo, o sistema deve verificar:
   - Se o ID é múltiplo de 3 e de 5 ao mesmo tempo: contabilizar como "Auditoria Crítica" e somar o valor desse ID a um acumulador total de críticos.
   - Se o ID é múltiplo apenas de 3: contabilizar como "Revisão Fiscal".
   - Se o ID é múltiplo apenas de 5: contabilizar como "Revisão Logística".
   - Os demais números devem ser ignorados na contagem.
5. Ao final do processamento, exibir o resumo contendo:
   - Quantidade de pedidos em Revisão Fiscal.
   - Quantidade de pedidos em Revisão Logística.
   - Quantidade de pedidos em Auditoria Crítica.
   - A soma total dos IDs classificados como Auditoria Crítica.
"""
numero_inicial = int(input("Digite o número inicial: "))
numero_final = int(input("Digite o número final: "))
auditoria_critica = 0
acumulador_critica = 0
revisao_fiscal = 0
revisao_logistica = 0

if numero_final < numero_inicial:
    print("Intervalo inválido!")
else:
    for i in range(numero_inicial, numero_final +1):
        if i % 3 == 0 and i % 5 == 0:
            acumulador_critica+=i 
            auditoria_critica +=1
        elif i % 3 == 0:
            revisao_fiscal+=1
        elif i % 5 == 0:
            revisao_logistica+=1
print(f"- Quantidade de pedidos em Revisão Fiscal. {revisao_fiscal}\n- Quantidade de pedidos em Revisão Logística. {revisao_logistica}\n- Quantidade de pedidos em Auditoria Crítica.{auditoria_critica} \n- A soma total dos IDs classificados como Auditoria Crítica. {acumulador_critica}")


