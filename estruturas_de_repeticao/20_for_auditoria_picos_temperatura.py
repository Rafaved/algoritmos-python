"""
Arquivo: 20_for_auditoria_picos_temperatura.py

Desafio 04 (Bloco 1 - FOR com Estado Anterior): Monitoramento de Picos Térmicos em Data Center
Objetivo: Registrar leituras consecutivas de temperatura de um servidor, identificar eventos de superaquecimento e detectar variações bruscas entre medições seguidas.

Regras de Negócio:
1. O sistema deve perguntar ao usuário quantas leituras de temperatura serão registradas.
2. Caso a quantidade de leituras seja menor ou igual a zero, o sistema deve exibir "Quantidade de leituras inválida." e encerrar.
3. Para cada leitura (da 1ª até a última), o sistema deve solicitar o valor da temperatura atual (em °C) e processar:
   - Acumular o valor para calcular a temperatura média ao final.
   - Identificar a maior temperatura registrada no período.
   - Contabilizar quantas leituras ultrapassaram o limite crítico de 75.0 °C.
   - A partir da 2ª leitura em diante, verificar se houve um salto brusco (aumento maior ou igual a 5.0 °C em relação à leitura imediatamente anterior) e contabilizar a quantidade de saltos bruscos detectados.
4. Ao final de todas as leituras, o sistema deve exibir um relatório contendo:
   - Temperatura média do período (com duas casas decimais).
   - Maior temperatura registrada (com duas casas decimais).
   - Quantidade de leituras acima de 75.0 °C.
   - Quantidade de saltos bruscos detectados.
"""

leitura_de_temperatura = int(input("Quantas leituras de temperatura será registrada: "))
maior_temp = 0
limite_critico = 0
aumento_brusco = 0
salto_brusco = 0
soma_temp = 0

if leitura_de_temperatura <= 0:
    print("Quantidade de leituras inválida.")
else:
    for i in range(1, leitura_de_temperatura + 1):
        temp_atual = float(input("\nDigite o valor da temperatura atual em °C: "))
        soma_temp += temp_atual
        if maior_temp < temp_atual:
            maior_temp = temp_atual
        if temp_atual > 75:
            limite_critico +=1
        if i > 1:
            aumento_brusco = temp_atual - temp_antiga
            if aumento_brusco >= 5:
                salto_brusco += 1
        temp_antiga = temp_atual
    temp_media = soma_temp / i
    print(f"Temperatura média {temp_media:.2f}°C\nMaior temperatura registrada {maior_temp:.2f}°C\nQuantidade de leituras acima de 75.0 °C {limite_critico}\nQuantidade de saltos bruscos detectados {salto_brusco}")





