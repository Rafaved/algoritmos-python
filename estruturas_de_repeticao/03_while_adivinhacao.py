"""
Exercício 03 - Jogo da Adivinhação

Objetivo:
Criar um jogo onde o sistema tem um número secreto de 1 a 10 e o usuário precisa adivinhar. O jogo só acaba quando ele acertar.

Regras de Negócio:
1. Defina um número secreto fixo no código (exemplo: 7).
2. Inicie um laço de repetição infinito.
3. Dentro do laço, peça para o usuário tentar adivinhar o número.
4. Verifique a entrada:
   - Se ele acertar, exiba uma mensagem de parabéns e acione a quebra do laço.
   - Se ele errar, exiba uma mensagem de erro e deixe o laço rodar novamente.
"""

import random

secreto = random.randint(1, 10)
tentativas = 1

while True:
    adivinhacao = int(input("Adivinhe o número de 1 a 10 do sistema: "))
    tentativas+=1
    if adivinhacao != secreto:
        print("Número errado tente novamente!!")
    else:
        print(f"Parabéns você acertou o número com {tentativas - 1} tentativas")
        break