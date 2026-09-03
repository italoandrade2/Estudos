# Adicionando novos contatos
# Nome: Italo Andrade Costa
# 25/05/2026 - Versão 1.0

with open('contatos.txt', 'a', encoding='utf-8') as arquivo:
    nome1 = input('Digite um nome: ')
    nome2 = input('Digite outro nome: ')

    arquivo.write(f'{nome1}\n')
    arquivo.write(f'{nome2}\n')

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())