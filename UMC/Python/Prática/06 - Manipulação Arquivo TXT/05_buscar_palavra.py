# Buscar uma palavra no arquivo
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

busca = "Carlos"

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for num, linha in enumerate(arquivo, 1):
        if busca.lower() in linha.lower():
            print(f"Linha {num}: {linha.strip()}")
