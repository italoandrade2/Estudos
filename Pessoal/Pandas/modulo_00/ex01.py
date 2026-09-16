import pandas as pd

dados = {
    "nome": ["Rafael", "Ana", "Paulo", "Júlia", "Carlos"],
    "idade": [18, 17, 19, 21, 24],
    "curso": ["Administração", "Direito", "Engenharia", "Enfermagem", "Informárica"]
}

alunos = pd.DataFrame(dados)

print(alunos)