# Simulação de Investimento
# Nome: Italo Andrade Costa
# 08/04/2026 - Versão 1.0

valor = float(input('Qual o valor investido?: R$'))
meses = int(input('Quantos meses de investimento?: '))

if meses <= 5:
    taxa = 0.005
elif meses <= 12:
    taxa = 0.008
else:
    taxa = 0.012

invest = valor*(1+taxa)**meses

if valor > 10000:
    invest *= 1.001

print(f'O valor atual é R${invest:.2f}.')