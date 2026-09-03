# Desconto de Produto
# Nome: Italo Andrade Costa
# 12/03/2026 - Versão 1.0

prod = float(input("Digite o valor do produto: R$"))
desc = int(input("Digite o valor do desconto: "))
desconto = prod*(desc/100)

texto = f"""Segue abaixo os valores solicitados:

Valor do produto: R${prod:.2f}
Porcentagem: {desc}%
Valor do desconto: R${desconto:.2f}
Valor final: R${prod-desconto:.2f}
"""

print(texto)