"""
Desafio 14: Reajuste Salarial
Objetivo: Calcular o novo salário de um funcionário com base em faixas de aumento.
Regras de Reajuste:
- Até R$ 1.500: +15%
- De R$ 1.500,01 a R$ 3.000: +10%
- Acima de R$ 3.000: +5%
"""
salario = float(input("Para sabermos o seu reajuse salarial, digite seu salário:"))
reajuste = 0

if salario <= 1.500:
    reajuste = salario + (salario * 0.15)
    print(f"O seu salario com o reajuste ficaria R${reajuste:.2f}")
elif salario <= 3.000:
    reajuste = salario + (salario * 0.10)
    print(f"O seu salario com o reajuste ficaria R${reajuste:.2f}")
else:
    reajuste = salario + (salario * 0.05)
    print(f"O seu salario com o reajuste ficaria R${reajuste:.2f}")