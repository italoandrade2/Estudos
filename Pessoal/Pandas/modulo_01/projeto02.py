import pandas as pd

funcionarios = pd.DataFrame ({
    "nome": ["Ana", "João", "Marcelo", "Júlia", "Maria", "Carlos", "Rodrigo", "Carla", "Beatriz", "Pietro"],
    "idade": [24, 32, 27, 29, 19, 21, 35, 37, 26, 30],
    "cargo": ["Auxiliar Administrativo", "Vendedor", "Vendedor", "Auxiliar de Limpeza", "Cozinheiro", "Auxiliar Administrativo", "Assistente Administrativo", "Gerente", "Vendedor", "Vendedor"],
    "salario": [2200.00, 3400.00, 3400.00, 3100.00, 4300.00, 2200.00, 3300.00, 5200.00, 3400.00, 3400.00],
    "departamento": ["Administrativo", "Vendas", "Vendas", "Geral", "Cozinha", "Administrativo", "Administrativo", "Administrativo", "Vendas", "Vendas"],
    "ativo": [True, False, True, True, True, False, True, True, False, True]
})

print(funcionarios)
print(funcionarios.head())
print(funcionarios.tail())
print(funcionarios.shape)
print(funcionarios.columns)
print(funcionarios.index)
print(funcionarios.dtypes)
print(funcionarios.info())
print(funcionarios.describe())