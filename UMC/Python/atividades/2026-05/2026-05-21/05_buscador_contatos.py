# Buscador de contatos
# Nome: Italo Andrade Costa
# 25/05/2026 - Versão 1.0

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    nomes = [linha.strip().capitalize() for linha in arquivo]

while True:
    nome = input('Digite um nome ou "sair" para finaizar: ').capitalize()
        
    if nome == 'Sair':
        print('Programa finalizado.')
        break
    
    if nome in nomes:
        linha = nomes.index(nome) + 1
        print(f'Encontrado na linha {linha}: {nome}')