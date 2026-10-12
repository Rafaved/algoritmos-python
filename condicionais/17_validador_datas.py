"""
Desafio 17: Validador de Datas Completo
Objetivo: Validar se uma data informada (dia, mês e ano) existe no calendário.
Regras de Negócio:
- Considerar os meses que terminam em 30 ou 31 dias.
- Considerar a regra do ano bissexto para validar se fevereiro tem 28 ou 29 dias.
"""
dia = int(input("Digite o dia: "))
mês = input("Digite o mês: ").lower() .strip( )
ano = int(input("Digite o ano: "))


if dia < 1:
    print("Dia inválido")
elif ano < 0:
    print("Ano inválido")
elif mês == "abril" or mês == "junho" or mês == "setembro" or mês == "novembro":
    if dia >= 1 and dia <= 30:
        print(f"Data válida: {dia} de {mês} de {ano}.")
    else:
        print(f"Data inválida! {mês.capitalize()} só tem 30 dias.")

elif mês == "janeiro" or mês == "março" or mês == "maio" or mês == "julho" or mês == "agosto" or mês == "outubro" or mês == "dezembro":
    if dia >= 1 and dia <= 31:
        print(f"Data válida: {dia} de {mês} de {ano}.")
    else:
        print(f"Data inválida! {mês.capitalize()} só tem 31 dias.")

elif mês == "fevereiro":
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto")
        if dia >= 1 and dia <= 29:
            print(f"Data válida: {dia} de {mês} de {ano}.")
        else:
            print(f"Data inválida! Em ano bissexto, fevereiro só vai até o dia 29.")
    else:
        print(f"O ano {ano} não é bissexto")
        if dia >= 1 and dia <= 28:
            print(f"Data válida: {dia} de {mês} de {ano}.")
        else:
            print(f"Data inválida! Em ano não bissexto, fevereiro só vai até o dia 28.")

else:
    print("Mês inválido, tente digitar novamente")
