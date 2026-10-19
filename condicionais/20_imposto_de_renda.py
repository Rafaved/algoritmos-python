"""
Desafio 20: Simulador de Imposto de Renda Progressivo
Objetivo: Calcular o IR devido com base em faixas escalonadas.
Regras de Negócio (O imposto incide APENAS sobre a parcela do salário que exceder a base anterior):
- Até R$ 2.000: Isento.
- De R$ 2.000,01 a R$ 3.500: 10% sobre o que passar de 2.000.
- De R$ 3.500,01 a R$ 5.000: 15% sobre o que passar de 3.500 + imposto da faixa anterior.
- Acima de R$ 5.000: 20% sobre o que passar de 5.000 + impostos acumulados das faixas anteriores.
"""

salario = float(input("Qual sua faixa salárial: "))
imposto = 0

if salario <= 2000:
    print("Como seu salário é até 2000, você é isenta de impostos.")
else:
    if salario > 2000:
        imposto = (salario - 2000) * 0.1
        print(f"Com seu salário passa de R$2000,00 o seu imposto é de {imposto:.2f}")
    elif salario > 3500:
        imposto = ((salario - 3500) * 0.15) + 150
        print(f"Com seu salário passa de R$3500,00 o seu imposto é de {imposto:.2f}")
    elif salario > 5000: 
        imposto = ((salario - 5000) * 0.2) + 375
        print(f"Com seu salário passa de R$5000,00 o seu imposto é de {imposto:.2f}")