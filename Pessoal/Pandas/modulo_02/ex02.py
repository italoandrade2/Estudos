import pandas as pd

produtos = pd.DataFrame({
    "produto": ["Mouse", "Teclado", "Monitor", "Notebook", "Headset"],
    "categoria": ["Periférico", "Periférico", "Monitor", "Computador", "Periférico"],
    "preco": [80, 120, 900, 3500, 250],
    "estoque": [50, 30, 10, 5, 20]
})

print(produtos.iloc[0:3])
print(produtos.iloc[0:3, 0:2])
print(produtos.iloc[1:4])
print(produtos.iloc[1:4, [0, 2]])
print(produtos.iloc[3,2])

print(produtos[produtos["preco"] > 500])    # Monitor (900) e Notebook (3500)
print(produtos[produtos["preco"] < 500])    # Mouse (80), Teclado (120) e Headset (250)
print(produtos[produtos["estoque"] >= 20])  # Mouse (50), Teclado (30) e Headset (20)
print(produtos[produtos["estoque"] <= 10])  # Monitor (10) e Notebook (5)
print(produtos[produtos["preco"] == 120])   # Teclado
print(produtos[produtos["preco"] != 120])   # Mouse, Monitor, Notebook e Headset