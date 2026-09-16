import pandas as pd

dados = {
    "nome": ["Ana", "João", "Carlos"],
    "idade": [25, 31, 22],
    "salario": [3500.00, 4200.00, 2800.75],
    "ativo": [True, True, False]
}

df = pd.DataFrame(dados)

print(df.dtypes)