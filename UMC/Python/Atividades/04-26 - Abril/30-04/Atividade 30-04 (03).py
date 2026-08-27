# Controle de Estoque com While
# Nome: Italo Andrade Costa
# 04/05/2026 - Versão 1.0

est1 = 100

while True:
    print(f'O estoque atual é de {est1} produtos.')
    acao = input('Qual será a ação desejada (a/r/sair): ').strip().lower()
        
    if acao == 'a':
        est1 += 1
    elif acao == 'r':
        if est1 > 0:
            est1 -= 1
        else:
            print('Erro. Não é permitido estoque negativo.')
    elif acao == 'sair':
        print('Finalizando programa...')
        break
    else:
        print('Erro. Ação inválida. Tente novamente.')
