# Gerenciador de Lista de Compras
# Nome: Italo Andrade Costa
# 04/05/2026 - Versão 1.0

lista = []
print('A lista está vazia.')

while True:
    texto = '''
    1) Adicionar item
    2) Remover item
    3) Listar todos os itens com numeração
    4) Sair
     
     Qual ação deseja realizar?: '''
    
    acao = input(texto)

    if acao == "1":
        item = str(input('\nDigite o item a ser adicionado: '))
        lista.append(item)
        print('\nItem adicionado!')
    elif acao == '2':
        item = str(input('\nDigite o item a ser removido: '))
        if item in lista:
            lista.remove(item)
            print('\nItem removdo!')
        else:
            print('\nItem não encontrado na lista.')
    elif acao == '3':
        if len(lista) == 0:
            print('\nLista vazia.')
        else:
            print('\nLista de compras: ')
            for i, item in enumerate(lista, start=1):
                print(f'{i} - {item}')
    elif acao == '4':
        print('Finalizando programa...')
        break

    else:
        print('Erro. Digite uma ação válida.')
        