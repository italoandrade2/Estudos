# Escrever em um arquivo TXT
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana Silva\n")
    arquivo.write("Bruno Costa\n")
    arquivo.write("Carlos Mendes\n")

print("Arquivo criado com sucesso!")