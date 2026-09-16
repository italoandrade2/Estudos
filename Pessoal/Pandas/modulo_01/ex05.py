import pandas as pd

dados = [["Mouse", 80], ["Teclado", 120], ["Monitor", 900], ["Headset", 250]]

produtos = pd.DataFrame(dados, columns=["produto", "preco"])

print(produtos)
print(produtos["produto"])
print(produtos["preco"])