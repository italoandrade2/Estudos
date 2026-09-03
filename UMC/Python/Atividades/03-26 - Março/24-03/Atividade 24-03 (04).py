# Percentual de Aumento de Salário
# Nome: Italo Andrade Costa
# 24/03/2026 - Versão 1.0

sal1 = float(input('Digite o salário do funcionário: R$'))
perc = int(input('Digite o percentual de aumento: '))
aum = sal1*(perc/100)
sal2 = sal1 + aum

texto = f'''Salário anterior: R${sal1:.2f}
Percentual de aumento: {perc}%
Valor do aumento: R${aum:.2f}
Salário novo: R${sal2:.2f}'''

print(texto)