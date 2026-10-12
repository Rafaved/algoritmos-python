"""
Desafio 11: Análise de Empréstimo Imobiliário
Objetivo: Validar a aprovação de um financiamento.
Regras de Negócio:
- Receber o valor do imóvel, salário do comprador e anos para pagar.
- Calcular a parcela mensal.
- O empréstimo só é aprovado se a parcela não ultrapassar 30% do salário.
"""

imovel = float(input("Digite o valor do imovel: "))
salario = float(input("Digite o seu salário por mês: "))
ano = int(input("Em quantos anos voce quer pagar: "))
parcela = imovel / (ano * 12)
emprestimo = salario * 0.30

if parcela > emprestimo:
    print("Negado! A parcela ficou muito cara pro seu salário.")
else:
    print("Aprovado! Pode assinar,")
