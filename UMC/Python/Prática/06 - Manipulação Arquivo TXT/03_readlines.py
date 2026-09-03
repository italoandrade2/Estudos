# Ler linha por linha com readlines()
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

for i, linha in enumerate(linhas, 1):
    print(f"Aluno {i}: {linha.strip()}")