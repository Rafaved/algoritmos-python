"""
Exercício 08 - Jogo da Adivinhação (Nível Médio)

Objetivo:
Criar um jogo onde o computador escolhe um número aleatório de 1 a 100 e o usuário deve adivinhar qual é.

Regras de Negócio:
1. Crie um laço de repetição (while) que peça continuamente para o usuário digitar um palpite numérico.
2. A cada palpite digitado, adicione +1 à variável de tentativas.
3. Use a lógica condicional (if/elif/else) para comparar o palpite do usuário com o número secreto:
   - Se o palpite for igual: Imprima "Parabéns! Você acertou..." e encerre com break.
   - Se o palpite for MAIOR: Imprima "O número secreto é menor."
   - Se o palpite for MENOR: Imprima "O número secreto é maior."
"""
import random

secreto = random.randint(1, 100)
tentativas = 0


while True:
   adivinhacao = int(input("Adivinhe o numéro de 1 a 100:\n"))
   tentativas +=1 
   if adivinhacao > secreto:
      print("O número secreto é menor.")
   elif adivinhacao < secreto:
      print("O número secreto é maior.")
   else:
      print(f"Parabéns! Você acertou, com {tentativas} tentativas")
      break