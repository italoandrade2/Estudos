# Remover contato
# Nome: Italo Andrade Costa
# 28/05/2026 - Versão 1.0

remove = input('Contato a remover: ')

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

nova_lista = [linha for linha in linhas if remove not in linha]

if len(nova_lista) == len(linhas):
    print('Nome não encontrado.')
else:
    with open('contatos.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(nova_lista)
        print(f'"{remove}" removido com sucesso!')