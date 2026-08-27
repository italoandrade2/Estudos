# Verificador de Número Primo
# Nome: Italo Andrade Costa
# 04/05/2026 - Versão 1.0

while True:
    num = int(input('Digite um número: '))

    if num <= 0:
        print('Erro. Digite um número positivo.')
    elif num == 1:
        print('Esse não é um número primo.')
    else:
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break

        if primo:
            print('Esse é um número primo.')
        else:
            print('Esse não é um número primo.')

    acao = input('Deseja continuar a operação (s/n)?: ').strip().lower()

    if acao == 's':
        print('Reiniciando...')
    elif acao == 'n':
        print('Finalizando programa...')
        break
    else:
        print('Erro. Digite uma ação válida.')
