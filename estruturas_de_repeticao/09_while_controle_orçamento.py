"""
Exercício 09 - Controle de Orçamento de Transporte Corporativo (Nível Difícil)

Objetivo:
Simular um sistema para a área de compras. O programa gerencia o saldo de "caixinha" 
para contas de transporte corporativo (como 99 ou Uber) e recebe os valores das corridas 
até que o usuário encerre os lançamentos ou o orçamento estoure.

Regras de Negócio:
1. Inicie o programa com um orçamento fixo, por exemplo, R$ 500.00 e um contador de corridas zerado.
2. Crie um laço (while) que peça continuamente o valor da corrida ou a palavra "fechar".
3. Lembre-se de sanitizar o texto (.lower()) para evitar que o código quebre.
4. Se o usuário digitar "fechar", o laço deve ser encerrado.
5. Se for um número (uma corrida):
   - Subtraia o valor do orçamento.
   - Adicione +1 ao contador de corridas.
6. REGRA DE BLOQUEIO (Dentro do laço): Logo após subtrair, verifique se o orçamento ficou menor que zero. 
   Se sim, imprima "ALERTA: Orçamento estourado!" e interrompa o laço (break) na hora.
7. No final (fora do laço), imprima o resumo: Quantas corridas foram registradas e o saldo final.
"""
orcamento = 500
contador_corridas = 0
pagamento = 0

while True:
    pergunta = input("Se não quiser pedir corrida digite FECHAR, se quiser digite o valor da corrida!!!\n").lower()
    if pergunta == "fechar":
        print("Encerrando sistema")
        break
    else:
        valor_corrida = float(pergunta)
        if valor_corrida > orcamento:
            print("O valor da corrida ficou maior que o seu próprio orçamento!!!")
            break
        else:
            contador_corridas += 1
            orcamento -= valor_corrida
            print(f"O valor da corrida foi contabilizado e subtraido do seu orçamento!!!")
print(f"O total de corridas foi de {contador_corridas} e o saldo final ficou de R${orcamento}")
