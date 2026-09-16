import pandas as pd

alunos = pd.DataFrame({
    "nome": ["Italo", "João", "Maria", "Carlos"],
    "idade": [22, 21, 25, 23],
    "curso": ["ADS", "ADS", "SI", "Engenharia de Dados"]
})

print(alunos)
print(alunos["nome"])
print(alunos["curso"])