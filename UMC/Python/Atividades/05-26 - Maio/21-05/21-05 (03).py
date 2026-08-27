# Enumeração de lista 
# Nome: Italo Andrade Costa
# 25/05/2026 - Versão 1.0

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    
for numero, nome in enumerate(linhas, start=1):
    print(f'{numero}. {nome.strip()}')
