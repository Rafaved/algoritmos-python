"""
Exercício 07 - Monitor de Temperaturas (Nível Médio)

Objetivo:
Criar um programa que lê várias temperaturas continuamente e, quando o usuário decidir parar, calcula a média de todas elas.

Regras de Negócio:
1. Inicie um laço que permita ao usuário digitar temperaturas numéricas repetidas vezes.
2. Crie uma forma de o usuário avisar que deseja encerrar a leitura (por exemplo, digitando a palavra "sair").
3. Lembre-se que você vai precisar de ferramentas para sanitizar esse texto (como fez no exercício anterior) para evitar que o código quebre.
4. Enquanto o usuário não digitar "sair", o programa deve acumular a soma das temperaturas e também contar quantas temperaturas foram digitadas.
5. Quando o laço for encerrado, calcule e exiba a média (soma dividida pela quantidade).
"""
soma_temperatura = 0
temperatura = 0
media = 0
contagem = 0

while True:
    temperatura = input("Digite a Temperatura ou digite a palavra SAIR caso queira ver a média:\n").lower()
    if temperatura == "sair":
        if contagem > 0:
            media = soma_temperatura / contagem
            print(f"A média das temperaturas é de {media}")
        else:
            print("Nenhuma temperatura foi informada")
        break
    else:
        valor_numero = float(temperatura)
        soma_temperatura+= valor_numero
        contagem+=1
        