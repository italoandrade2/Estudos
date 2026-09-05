# Contar palavras e linhas de um arquivo
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.splitlines()
palavras = conteudo.split()
caracteres = len(conteudo)

print(f"Linhas: {len(linhas)}")
print(f"Palavras: {len(palavras)}")
print(f"Caracteres: {caracteres}")