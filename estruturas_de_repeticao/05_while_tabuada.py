"""
Exercício 05 - Tabuada com Limite

Objetivo:
Criar um programa que calcula a tabuada de um número escolhido pelo usuário, indo apenas do 1 ao 10.

Regras de Negócio:
1. Fora do laço, peça para o usuário digitar de qual número ele quer ver a tabuada.
2. Crie algo para servir de multiplicador (começando no número 1).
3. Crie um laço de repetição com condição (sem usar a quebra infinita). O laço deve rodar apenas enquanto o multiplicador for menor ou igual a 10.
4. Dentro do laço, exiba o resultado da multiplicação no formato "X x Y = Z".
5. Ainda dentro do laço, não se esqueça de alterar o valor do seu multiplicador para evitar um loop infinito.
"""

numero = int(input("Digite o número do qual você quer ver a tabuada de 1 a 10: "))
tabuada = 0
contagem = 1
while contagem <= 10:
    tabuada = numero + tabuada
    contagem += 1
    print(f"A tabuada  do {numero} é {numero} x {contagem - 1} = {tabuada}")