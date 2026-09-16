import pandas as pd

dados = {
    "nome": ["Ana", "João", "Carlos"],
    "idade": [25, 31, 22],
    "cidade": ["São Paulo", "Mogi das Cruzes", "Suzano"]
}

df = pd.DataFrame(dados)

print(df)

print(pd.__version__)