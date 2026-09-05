# Leitura de arquivo
# Nome: Italo Andrade Costa
# 25/05/2026 - Versão 1.0

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())

print('\nFim do arquivo.')