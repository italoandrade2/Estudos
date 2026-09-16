import pandas as pd

produtos = pd.DataFrame({
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Headset", "Webcam", "SSD", "Memória RAM"],
    "categoria": ["Informática", "Periféricos", "Periféricos", "Informática", "Periféricos", "Periféricos", "Componentes", "Componentes"],
    "quantidade": [2, 10, 5, 4, 7, 6, 8, 12],
    "preco": [3500.0, 80.0, 120.0, 900.0, 250.0, 180.0, 400.0, 300.0]
})

print(produtos.head())
print(produtos.tail(3))
print(produtos.shape)
print(produtos.columns)
print(produtos.dtypes)
print(produtos.info())
print(produtos.describe())