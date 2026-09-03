# Ler todo o conteúdo de um arquivo
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)