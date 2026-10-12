"""
Desafio 03: Monitor de Temperatura
Objetivo: Ler a temperatura ambiente em graus Celsius e classificar a saída: 
- Frio (< 15°C)
- Agradável (15°C a 25°C)
- Quente (> 25°C)
"""

temperatura = int(input("Qual a temperatura ambiente: "))

if temperatura < 15:
    print(f"A temperatura {temperatura} está frio")
elif temperatura <= 25:
    print(f"A temperatura {temperatura} está agradável")
else:
    print(f"A temperatura {temperatura} está quente")