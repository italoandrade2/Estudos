# Adicionar conteúdo sem apagar (append)
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Daniela Rocha\n")

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())