# Remover linha específica do arquivo
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

remover = "Carlos Mendes"

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

filtradas = [l for l in linhas if remover not in l]

with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(filtradas)

print(f'"{remover}" removido do arquivo.')