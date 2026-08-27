# Salvar em txt
# Nome: Italo Andrade Costa
# 28/05/2026 - Versão 1.0

lista = ['Arroz - 2kg', 'Feijão - 1kg', 'Macarrão - 500g', 'Azeite - 1 frasco', 'Ovos - 12 unidades', 'Leite - 2 litros']

with open('compras.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        produto = input('Adicione um item na lista: ')

        if produto.lower() == "pronto":
            print('Lista de compras salva!')
            break
    
        lista.append(produto)
        arquivo.write(produto + '\n')