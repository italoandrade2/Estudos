import pandas as pd

vendas = pd.DataFrame({
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Headset", "SSD"],
    "categoria": ["Informática", "Periféricos", "Periféricos", "Informática", "Periféricos", "Componentes"],
    "quantidade": [2, 15, 8, 5, 12, 10],
    "preco": [3500, 80, 120, 900, 250, 400]
})

print(vendas[["produto", "preco"]])
print(vendas[vendas["preco"] > 300])
print(vendas.loc[vendas["quantidade"] > 10, ["produto", "quantidade"]])