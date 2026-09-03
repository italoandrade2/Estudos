# Simulador de Caixa Eletrônico
# Nome: Italo Andrade Costa
# 05/05/2026 - Versão 1.0

extrato = []
saldo = 1000.00

while True:
    texto = '''
    1) Saque
    2) Depósito
    3) Extrato
    4) Sair
     
     Qual ação deseja realizar?: '''
    
    acao = input(texto)

    if acao == '1':
        valor = float(input('\nDigite o valor a ser sacado: R$'))
        saldo -= valor
        extrato.append(f'Saque de R${valor:.2f} \t Saldo = R${saldo:.2f}')

    elif acao == '2':
        valor = float(input('\nDigite o valor a ser depositado: R$'))
        saldo += valor
        extrato.append(f'Depósito de R${valor:.2f} \t Saldo = R${saldo:.2f}')

    elif acao == '3':
        print('\n--- EXTRATO ---\n')
        print('Saldo anterior: R$1000.00')
        for item in extrato:
            print(item)

    elif acao == '4':
        print('Finalizando programa...')
        break

    else:
        print('Erro. Digite uma ação válida.') 