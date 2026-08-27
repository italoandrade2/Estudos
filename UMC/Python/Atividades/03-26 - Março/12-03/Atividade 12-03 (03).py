valor = float(input("Digite o valor do produto: R$"))
prod = int(input("Digite a quantia de produtos: "))

texto = f"""Segue abaixo os dados da compra:

Valor do produto: R${valor}
Quantidade de produtos: {prod}
Valor total dos produtos: R${valor*prod:.2f}
"""

print(texto)