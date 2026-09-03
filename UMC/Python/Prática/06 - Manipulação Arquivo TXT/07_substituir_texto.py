# Substituir texto dentro do arquivo
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

novo = conteudo.replace("Bruno Costa", "Bruno Oliveira")

with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(novo)

print("Nome atualizado com sucesso!")