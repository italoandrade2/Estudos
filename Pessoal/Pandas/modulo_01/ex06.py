import pandas as pd

dados = [
    {"produto": "Notebook", "preco": 3500, "estoque": 10},
    {"produto": "Mouse", "preco": 80, "estoque": 50},
    {"produto": "Teclado", "preco": 120, "estoque": 30},
    {"produto": "Monitor", "preco": 900, "estoque": 15}
]

produtos = pd.DataFrame(dados)

print(produtos)
print(produtos.shape)
print(produtos.columns)
print(produtos.dtypes)