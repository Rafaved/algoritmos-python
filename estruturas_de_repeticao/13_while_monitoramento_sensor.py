"""
Arquivo: 13_while_monitoramento_sensor.py

Solicitação (Ticket): Pipeline de Telemetria de Sensores IoT
Setor: Engenharia de Dados / Infraestrutura

Requisitos da regra de negócio:
O sistema deve monitorar leituras contínuas de temperatura de um sensor industrial.
1. O laço `while True` deve pedir a leitura da temperatura em °C ou a palavra "sair".
2. Se o usuário digitar "sair", encerre o programa e exiba o relatório final.
3. Tratamento de anomalias (Dados corrompidos):
   - Temperaturas abaixo de -50°C ou acima de 150°C são anomalias do sensor.
   - O sistema NÃO deve encerrar o laço ao detectar uma anomalia. Ele apenas exibe "Leitura inválida descartada" e ignora esse valor nos cálculos.
4. Para as leituras VÁLIDAS:
   - Guarde a maior temperatura lida.
   - Guarde a menor temperatura lida.
   - Calcule a média de todas as temperaturas válidas.
5. No encerramento ("sair"), exiba: Total de leituras válidas, Maior temperatura, Menor temperatura e a Média das temperaturas.
"""
maior = 0 
menor = 0
media = 0
numeros = 0
quantidade = 0
while True:
    monitoramento = input("Coloque a temperatura em °C ou digite 'sair' ").lower()
    if monitoramento == "sair":
        print(f"Total de leituras válidas: {quantidade}\nMaior temperatura: {maior}\nMenor temperatuara:{menor}\nMédia das temperaturas: {media}")
        break

    valor_numero = float(monitoramento)
    
    if valor_numero < -50 or valor_numero > 150:
        print("Leitura inválida descartada")
    else:
        numeros += valor_numero
        quantidade += 1
        media = numeros / quantidade
        if quantidade == 1:
            maior = valor_numero
            menor = valor_numero
        else:
            if valor_numero > maior:
                maior = valor_numero
            if valor_numero < menor:
                menor = valor_numero
    
