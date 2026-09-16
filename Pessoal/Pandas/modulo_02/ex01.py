import pandas as pd

funcionarios = pd.DataFrame ({
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo"],
    "idade": [20, 25, 30, 22, 35],
    "cargo": ["Estagiário", "Analista", "Desenvolvedor", "Assistente", "Gerente"],
    "salario": [1500.00, 3000.00, 4500.00, 2200.00, 6000.00]
})

print(funcionarios["nome"])
print(funcionarios["salario"])
print(funcionarios[["nome", "cargo"]])
print(funcionarios[["nome", "idade", "salario"]])

print(funcionarios.loc[0])
print(funcionarios.loc[2])
print(funcionarios.loc[[1, 3]])
print(funcionarios.loc[[0, 2, 4]])

print(funcionarios.iloc[0])
print(funcionarios.iloc[2])
print(funcionarios.iloc[4])
print(funcionarios.iloc[0:3])
print(funcionarios.iloc[1:4])