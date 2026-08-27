# Estatísticas
# Nome: Italo Andrade Costa
# 28/05/2026 - Versão 1.0

with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

    linhas = conteudo.splitlines()
    palavras = conteudo.split()
    caracteres = conteudo.replace('\n', '')

    maior = max(linhas, key=len)

    print("="*5, "Estatisticas", "="*5)
    print('Linhas:', len(linhas))
    print('Palavras:', len(palavras))
    print('Caracteres:', len(caracteres))
    print('Nome mais longo:', maior)
