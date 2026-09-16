import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo", "Fernanda"],
    "idade": [20, 25, 30, 22, 28, 35],
    "salario": [2000.0, 2500.0, 3000.0, 2200.0, 2800.0, 3500.0]
}

funcionarios = pd.DataFrame(dados)

print(funcionarios)             # Retorna o DataFrame completo do dicionário
print(funcionarios.head())      # Retorna os 5 primeiros dados do DataFrame
print(funcionarios.tail())      # Retorna os 5 últimos dados do DataFrame
print(funcionarios.shape)       # Retorna a quantia de linhas e colunas do DataFrame
print(funcionarios.columns)     # Retorna os nomes das colunas do DataFrame
print(funcionarios.index)       # Retorna os dados dos índeces do DataFrame (onde começa, onde termina e quantos números pulam)
print(funcionarios.dtypes)      # Retorna os tipos de cada Series do DataFrame
print(funcionarios.info())      # Retorna as informações do DataFrame (quantas colunas, índeces, e quantos valores são nulos ou não)
print(funcionarios.describe())  # Retorna os dados numéricos do DataFrame (quantia total, média, máximo, mínimo, etc.)