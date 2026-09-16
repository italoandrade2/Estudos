import pandas as pd

funcionarios = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo", "Fernanda"],
    "idade": [19, 24, 31, 28, 35, 22],
    "cargo": ["Estagiário", "Analista", "Desenvolvedor", "Analista", "Gerente", "Estagiária"],
    "salario": [1500, 3000, 4500, 3200, 6000, 1600],
    "ativo": [True, True, True, False, True, True]
})

print(funcionarios[funcionarios["idade"] > 30])
print(funcionarios[funcionarios["idade"] < 25])
print(funcionarios[funcionarios["salario"] > 3000])
print(funcionarios[funcionarios["salario"] <= 1600])
print(funcionarios[funcionarios["salario"] == 3000])
print(funcionarios[~(funcionarios["salario"] == 3000)])

print(funcionarios[(funcionarios["idade"] > 25) & (funcionarios["salario"] > 3000)])
print(funcionarios[(funcionarios["idade"] < 25) | (funcionarios["salario"] > 5000)])
print(funcionarios[(funcionarios["idade"] >= 20) & (funcionarios["idade"] <= 30)])
print(funcionarios[(funcionarios["ativo"] == True) & (funcionarios["salario"] > 2000)])
print(funcionarios[~(funcionarios["ativo"] == True)])