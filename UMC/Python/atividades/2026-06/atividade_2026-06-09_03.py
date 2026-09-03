# Controle de Estoque
# Nome: Italo Andrade Costa
# 09/06/2026 - Versão 1.0

estoque = 5

print(f'Estoque atual: {estoque}\n')
print('Adicionar \t (a)')
print('Remover \t (r)')
print('Sair \t\t (sair)')

while True:

    acao = input('\nQual ação deseja realizar? ').lower()

    if acao == 'a':
        estoque += 1
        print(f'Estoque atual: {estoque}')

    elif acao == 'r':
        if estoque > 0:
            estoque -= 1
            print(f'Estoque atual: {estoque}')
        else:
            print('O estoque atual está zerado. Não é possível remover mais itens.')

    elif acao == 'sair':
        print('Finalizando programa...')
        break

    else:
        print('Ação inválida. Tente novamente:')