"""
Exercício 06 - Menu de Caixa Eletrônico

Objetivo:
Criar um menu interativo de banco que fica na tela continuamente até o cliente escolher a opção de sair.

Regras de Negócio:
1. Inicie um laço de repetição infinito.
2. Dentro do laço, exiba um menu com três opções numéricas: Ver Saldo, Depositar e Sair.
3. Peça para o usuário digitar a opção desejada.
4. Verifique a entrada usando condicionais (if/elif/else):
   - Se escolher a opção de saldo, exiba um valor fictício.
   - Se escolher a opção de depósito, exiba uma mensagem de sucesso.
   - Se escolher a opção de sair, exiba uma mensagem de despedida e acione a quebra do laço.
   - Se digitar qualquer outra coisa, exiba que a opção é inválida e deixe o menu aparecer de novo.
"""
saldo = 0
deposito = 0
while True:
    menu = input("Ver Saldo\nDepositar\nSair\nDigite qual opção você quer: ").lower()
    if menu == "ver saldo":
        print(f"Seu saldo é de R${deposito}\n")
    elif menu == "depositar":
        saldo = float(input("Digite o quanto você quer depositar: R$ "))
        deposito += saldo
        print(f"Seu depósito de R${deposito:.2f}\n")
    elif menu == "sair":
        print("Obrigado e volte sempre!!!")
        break
    else:
        print("Não foi reconhecido essa opção tente novamente!!!")
