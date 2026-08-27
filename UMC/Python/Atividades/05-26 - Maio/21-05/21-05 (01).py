# Adicionando nomes em arquivo
# Nome: Italo Andrade Costa
# 25/05/2026 - Versão 1.0

with open('contatos.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Alice\n')
    arquivo.write('Bruno\n')
    arquivo.write('Carlos\n')
    arquivo.write('Daniela\n')
    arquivo.write('Eduardo\n')

print('Contatos salvos!')