import pandas as pd

dados = {
    "nome": ["Rogério", "Carla", "Renata", "Marcello", "Vinícius"],
    "idade": [33, 26, 36, 47, 27],
    "cargo": ["Vendedor", "Auxiliar Administrativo", "Gerente", "Limpeza", "Suporte TI"],
    "salário": [3600, 1900, 4700, 2400, 3200]
}

funcionarios = pd.DataFrame(dados)

print(funcionarios)