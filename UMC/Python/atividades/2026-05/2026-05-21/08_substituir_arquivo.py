# Substituir contato
# Nome: Italo Andrade Costa
# 28/05/2026 - Versão 1.0

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

    antigo = input('Nome a substituir: ')

    if antigo in conteudo:
        novo = input('Novo nome: ')
        conteudo = conteudo.replace(antigo, novo)
        print(f'"{antigo}" atualizado para "{novo}" com sucesso!')
    else:
        print('Nome não encontrado.')

with open('contatos.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo)

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())