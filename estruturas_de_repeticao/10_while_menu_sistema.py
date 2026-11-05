"""
Exercício 10 - Menu Interativo de Sistema (Nível Chefe)

Objetivo:
Criar o "esqueleto" de um sistema de terminal corporativo, onde um menu de opções 
fica rodando infinitamente na tela até o usuário escolher a opção de sair.

Regras de Negócio:
1. Crie uma variável `total_gasto = 0`.
2. Crie um laço `while True`.
3. Logo no início do laço, peça para o usuário digitar uma opção do menu:
   [1] Registrar nova nota fiscal
   [2] Ver total gasto
   [3] Sair do sistema
4. Use if/elif/else para tratar a opção escolhida:
   - Se digitar "1": peça o valor da nota (float) e some ao `total_gasto`.
   - Se digitar "2": imprima o `total_gasto` atual.
   - Se digitar "3": imprima "Encerrando..." e quebre o laço (break).
   - Se digitar qualquer outra coisa: imprima "Opção inválida!" e o laço vai recomeçar sozinho.
"""

total_gasto = 0

while True:
    menu = int(input("\n\n[1] Registrar nova nota fiscal\n[2] Ver total gasto\n[3] Sair do sistema\nDigite o número da opção escolhida: "))
    if menu == 1:
        nota = float(input("Digite o valor da nota: "))
        total_gasto += nota
    elif menu == 2:
        print(f"\n\nO total gasto foi de R$ {total_gasto}")
    elif menu == 3:
        print("\n\nEncerrando...\n\n")
        break
    else:
        print("\n\nDigite o número dentre as opçoes apresentadas")