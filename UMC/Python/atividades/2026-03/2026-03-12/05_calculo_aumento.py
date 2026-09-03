# Cálculo de Aumento
# Nome: Italo Andrade Costa
# 12/03/2026 - Versão 1.0

est1 = int(input("Digite o estoque anterior: "))
porc = int(input("Digite a porcentagem de aumento: "))
porcentagem = porc/100
est2 = est1*(1.0+porcentagem)

texto = f"""Segue abaixo os dados de estoque:

Estoque anterior: {est1}
Porcentagem de aumento: {porc}%
Novo estoque: {int(est2)}
Quantia de produtos novos: {int(est2-est1)}
"""

print(texto)