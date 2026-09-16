import pandas as pd

funcionarios = pd.DataFrame({
    "nome": ["Roberto", "Paulo", "Thaís", "Hellen", "Welligton", "Caíque", "Mariana", "Juliana", "Bruno", "João"],
    "idade": [24, 21, 29, 32, 35, 19, 20, 22, 30, 27],
    "cargo": ["Gerente", "Auxiliar Administrativo", "Desenvolvedor Júnior", "Auxiliar de Limpeza", "Suporte Técnico", "Estagiário", "Estagiário", "Assistente Administrativo", "Vendedor", "Vendedor"],
    "departamento": ["Administrativo", "Administrativo", "TI", "Geral", "TI", "Administrativo", "Administrativo", "Administrativo", "Vendas", "Vendas"],
    "salario": [5200, 2100, 2600, 3100, 3800, 1200, 1200, 2900, 3500, 3500],
    "ativo": [True, False, True, True, True, True, False, True, False, True]
})

print(funcionarios[["nome", "departamento", "salario"]])
print(funcionarios[funcionarios["salario"] > 3000])
print(funcionarios[(funcionarios["idade"] >= 25) & (funcionarios["salario"] > 3000)])
print(funcionarios[funcionarios["departamento"] == "TI"])
print(funcionarios[(funcionarios["departamento"] == "TI") & (funcionarios["ativo"] == True)])
print(funcionarios[(funcionarios["idade"] < 25) | (funcionarios["salario"] > 5000)])
print(funcionarios.loc[funcionarios["salario"] > 3000, ["nome", "salario"]])
print(funcionarios.iloc[0:5, 0:3])
print(funcionarios[(funcionarios["idade"] > 30) & (funcionarios["ativo"] == True)])