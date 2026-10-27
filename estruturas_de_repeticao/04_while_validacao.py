"""
Exercício 04 - Validador de Dados de RH

Objetivo:
Criar um sistema que exige uma idade válida para o cadastro de um funcionário. O sistema bloqueia o avanço se a idade for impossível.

Regras de Negócio:
1. Inicie um laço de repetição infinito.
2. Peça para o usuário digitar a idade do funcionário.
3. Verifique a entrada:
   - Se a idade estiver entre 18 e 65 anos (inclusive), exiba "Cadastro aprovado" e acione a quebra do laço.
   - Caso contrário, exiba "Idade inválida" e deixe o laço pedir o dado novamente.
"""

while True:
    idade = int(input("Digite sua idade:"))
    if 18 <= idade <= 65:
        print(f"a sua idade de {idade} foi aprovado!!!")
        break
    else:
        print(f"sua idade de {idade} é inválida!! Cadastre novamente.")