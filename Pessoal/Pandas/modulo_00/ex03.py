import pandas as pd

dados = {
    "descricao": ["Banana", "Cenoura", "Abacaxi", "Uva", "Mamão", "Laranja"],
    "valor": [4.5, 6.99, 7.2, 2.75, 5.99, 3.5]
}

produtos = pd.DataFrame(dados)

print(produtos)