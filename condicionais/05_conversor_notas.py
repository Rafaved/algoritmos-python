"""
Desafio 05: Validador de Notas
Objetivo: Ler uma nota escolar de 0 a 10 e retornar o status final: 
- Aprovado (>= 7)
- Recuperação (5 a 6.9)
- Reprovado (< 5)
"""

nota = float(input("Digite o quanto você tirou na prova: "))

if nota >= 7:
    print(f"A nota {nota} é boa, você foi APROVADO!!!")
elif nota < 7:
    print(f"a nota {nota} é baixa, mas você ainda tem chance, RECUPERAÇÃO!!!")
else:
    print(f"A nota {nota} é muito baixa, você foi REPROVADO")