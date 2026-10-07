"""
Desafio 08: Calculadora Básica com Prevenção de Erros
Objetivo: Receber dois números e um operador (+, -, *, /).
Regras de Negócio:
- Executar o cálculo de acordo com o operador. 
- Bloquear divisão por zero com a mensagem "Erro: Divisão por zero".
- Avisar "Operação inválida" se o símbolo não for reconhecido.
"""

print("Bem-vindo a calculadora")
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador para fazer a conta, os operadore permitidos são:\n(+, -, *, /): ")
conta = 0

if operador == "+":
    conta = numero_1 + numero_2
    print(f"O resultado da conta é {conta}")
elif operador == "-":
    conta = numero_1 - numero_2
    print(f"O resultado da conta é {conta}")
elif operador == "*":
    conta = numero_1 * numero_2
    print(f"O resultado da conta é {conta}")
elif (operador == "/" ) and (numero_2 == 0):
    print("Erro: Divisão por zero")
elif operador == "/":
    conta = numero_1 / numero_2
    print(f"O resultado da conta é {conta}")
else:
    print("Digite um operador correto!")
