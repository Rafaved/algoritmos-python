"""
Arquivo: 15_while_simulador_metas.py

Solicitação (Ticket): Engine de Projeção de Investimentos e Metas
Setor: Business Intelligence / Engenharia de Dados Financeiros

Requisitos da regra de negócio:
Criar um simulador interativo de projeção de patrimônio e cálculo de tempo até atingir uma meta financeira.

1. Validação dos Parâmetros de Entrada (antes do loop):
   - Solicitar a Meta de Patrimônio em R$ (float). Se <= 0, exibir "Meta inválida!" e encerrar o programa.
   - Solicitar o Aporte Mensal fixo em R$ (float). Se <= 0, exibir "Aporte inválido!" e encerrar o programa.
   - Solicitar a Taxa de Rendimento Mensal em % (float, ex: 0.8 para 0,8%). Se <= 0, exibir "Taxa inválida!" e encerrar o programa.

2. Variáveis de Controle e Acumuladores (iniciar antes do loop):
   - mes = 0 (contador de meses decorridos)
   - saldo_atual = 0.0 (inicia em 0)
   - total_investido = 0.0 (soma apenas do dinheiro do bolso)
   - total_juros = 0.0 (soma apenas dos rendimentos)

3. Execução do Laço (`while`):
   - O laço deve rodar ENQUANTO `saldo_atual` for MENOR que a `meta` E o `mes` for MENOR que 600 (trava de segurança para limite de 50 anos / 600 meses).
   - A cada ciclo (mês):
     * Incremente +1 no `mes`.
     * Adicione o valor do aporte ao `saldo_atual` e acumule no `total_investido`.
     * Calcule o rendimento do mês: `rendimento_mes = saldo_atual * (taxa / 100)`.
     * Adicione o `rendimento_mes` ao `saldo_atual` e acumule no `total_juros`.

4. Relatório de Encerramento (exibir fora do loop):
   - Se o saldo atingiu ou superou a meta:
     * Calcule os anos e meses equivalentes (dica: anos = mes // 12, meses_restantes = mes % 12).
     * Exiba: "Meta atingida em X meses (Y anos e Z meses)!"
   - Se encerrou pela trava de 600 meses sem atingir a meta:
     * Exiba: "Meta não atingida dentro do limite operacional de 50 anos."
   - Exiba o detalhamento consolidado (formatado em R$ e duas casas decimais):
     * Saldo Final Acumulado
     * Total Investido do Bolso
     * Total Ganho em Juros
     * Porcentagem do Patrimônio vinda de Juros: `(total_juros / saldo_atual) * 100`
"""
meta = float(input("Digite a meta de Patrimônio em R$:\n"))
aporte = float(input("Digite o aporto mensal em R$:\n"))
taxa = float(input("Digite a taxa mensal do rendimento:\n"))
total_investido = 0
total_juros = 0
mes = 0
saldo_atual = 0

if meta <= 0:
  print("Meta inválida!")
elif aporte <= 0:
  print("Aporte inválido!")
elif taxa <= 0:
  print("Taxa inválida!")
else:
  while saldo_atual < meta and mes < 600:
    mes +=1
    saldo_atual += aporte
    total_investido += saldo_atual
    rendimento_mes = saldo_atual *(taxa/100)
    saldo_atual += rendimento_mes
    total_juros +=rendimento_mes
    if saldo_atual >= meta:
      ano = mes // 12 
      meses_restantes = mes % 12 
      print(f"Meta atingida em {mes} meses ({ano} anos e {meses_restantes} meses)!")
