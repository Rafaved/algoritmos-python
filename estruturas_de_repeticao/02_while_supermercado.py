"""
Exercício 03 - Caixa de Supermercado (Loop infinito e quebra)

Objetivo:
Criar um simulador de caixa de supermercado que vai somando os preços dos produtos continuamente, 
até que o funcionário digite o número 0 para encerrar o atendimento.

Regras de Negócio:
1. Antes de iniciar o atendimento, você precisará de algo para guardar e acumular a soma de tudo que será passado (começando zerado).
2. Inicie um laço de repetição infinito para que o caixa fique sempre pronto para o próximo produto.
3. Dentro do laço, peça para o usuário digitar o valor numérico do produto atual.
4. Verifique a entrada: se o valor digitado for exatamente 0, acione a quebra do laço para encerrar a compra.
5. Caso contrário, pegue o valor digitado e some ao seu acumulador.
6. Após sair do laço, exiba uma mensagem final mostrando o valor total que o cliente deve pagar.
"""

item = 1
soma = 0

while True:
    preco = float(input(f"Digite o valor do item {item}, quando não houver mais itens para passarr digite 0:  "))
    if preco > 0: 
        soma = preco + soma
        item+=1
    elif preco < 0:
        print(f"o valor do item {item} não pode ser negativo!!" )
        break
    else:
        item-=1
        print(f"o resultado das suas compras com {item} itens foi de R$ {soma:.2f} ")
        break