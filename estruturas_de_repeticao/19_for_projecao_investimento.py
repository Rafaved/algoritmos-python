"""
Arquivo: 19_for_projecao_investimento.py

Desafio 03 (Bloco 1 - FOR com range): Simulador de Projeção de Investimento
Objetivo: Calcular a evolução mensal de um investimento com aportes recorrentes e juros compostos ao longo de um período definido.

Regras de Negócio:
1. O sistema deve solicitar ao usuário:
   - O valor do aporte inicial (em R$).
   - O valor do aporte mensal recorrente (em R$).
   - A taxa de rendimento mensal (em %, por exemplo: 1.2 para 1,2% ao mês).
   - O prazo total do investimento (em meses inteiros).
2. Caso o prazo seja menor ou igual a zero, ou algum valor financeiro ou taxa seja negativo, o sistema deve exibir "Parâmetros inválidos para simulação." e encerrar.
3. Para cada mês do período (do mês 1 até o mês final, inclusive), o sistema deve:
   - Aplicar o rendimento mensal sobre o saldo acumulado atual.
   - Somar o aporte mensal recorrente ao saldo após o rendimento.
   - Exibir o saldo atualizado daquele mês formatado com duas casas decimais (ex: "Mês 1: R$ 1050.00").
4. Ao final da simulação, o sistema deve exibir um resumo consolidado contendo:
   - Total investido do próprio bolso (aporte inicial + soma de todos os aportes mensais).
   - Total ganho apenas em rendimentos (saldo final menos o total investido).
   - Saldo final acumulado.
"""
aporte_inicial = float(input("digite o aporte inicial em R$ "))
aporte_mensal = float(input("digite o aporte mensal recorrente em R$ "))
taxa_rendimento = float(input("digite também a taxa mensal do rendimento "))
prazo_total = int(input("digite também o prazo total do invesimento em meses: "))
saldo_total = aporte_inicial
investimento_total_do_bolso = 0 
ganho_rendimentos = 0

if prazo_total <= 0 or aporte_inicial < 0 or aporte_mensal < 0 or taxa_rendimento < 0:
    print("Parâmetros inválidos para simulação.")
else:
    for i in range(1, prazo_total + 1):
        saldo_total += saldo_total * (taxa_rendimento / 100)
        saldo_total += aporte_mensal
        print(f"Mês {i}: R$ {saldo_total:.2f}\n")
    investimento_total_do_bolso = aporte_inicial + (aporte_mensal * prazo_total)
    ganho_rendimentos = saldo_total - aporte_mensal
    print(f"Total investido do próprio bolso R$ {investimento_total_do_bolso:.2f}\nTotal do ganho apenas em rendimentos R$ {ganho_rendimentos:.2f}\nSaldo final R$ {saldo_total:.2f}")