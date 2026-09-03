# Cálculo de Lucro
# Nome: Italo Andrade Costa
# 12/03/2026 - Versão 1.0

valor = float(input("Digite o valor do produto: R$"))
custo = float(input("Digite o custo do produto: R$"))
lucro = valor-custo

texto = f"""Segue abaixo os dados do produto:

Valor do produto: R${valor:.2f}
Custo do produto: R${custo:.2f}
Lucro da venda: R${lucro:.2f}
Porcentagem de lucro: {int((lucro/custo)*100)}%
"""

print(texto)