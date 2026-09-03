# Sistema de reserva de apartamento
# Italo Andrade Costa
# 30/03/2026 - Versão 1.0

while True:
    #Exibição de tabela
    texto1 = '''Bem-vindo! Segue abaixo os valores de nossos apartamentos:

    Nº de                  Diária                  Diária
    pessoas                Tipo 1                  Tipo 2
    [1]                   R$20,00                  R$25,00
    [2]                   R$28,00                  R$34,00
    [3]                   R$35,00                  R$42,00
    [4]                   R$42,00                  R$50,00
    [5]                   R$48,00                  R$57,00
    [6]                   R$53,00                  R$63,00'''

    print(texto1)

    #Tabela de preços
    precos = {
        1: {1: 20, 2: 28, 3: 35, 4: 42, 5: 48, 6: 53},
        2: {1: 25, 2: 34, 3: 42, 4: 50, 5: 57, 6: 63}
    }

    while True:
        while True:
            try:
                #Escolha do apartamento
                tipo = int(input('\nDigite o tipo de apartamento que você deseja (1 ou 2): '))
                if tipo in (1, 2):
                    break
                else:
                    print('Resposta inválida. Tente novamente.')
            except ValueError:
                print('Digite apenas números (1 ou 2).')
        
        while True:
            try:
                #Escolha da quantia de pessoas
                pessoas = int(input('Digite a quantidade de pessoas que ocuparão o apartamento (1 a 6): '))
                if pessoas in range(1, 7):
                    break
                elif pessoas == 0:
                    print('Digite um número maior que zero.')
                else:
                    print('O limite máximo é de 6 pessoas.')
            except ValueError:
                print('Digite apenas números (1 a 6).')

        while True:
            try:
                #Escolha da quantia de dias
                dias = int(input('Quantos dias de estadia? (1 a 7): '))
                if dias in range(1, 8):
                    break
                elif dias == 0:
                    print('Digite um número maior que zero.')
                else:
                    print('O limite máximo de dias é 7.')
            except ValueError:
                print('Digite apenas números (1 a 7).')

        #Cálculo do total da estadia
        diaria = precos[tipo][pessoas]
        diaporpes = diaria*pessoas
        total = diaporpes*dias

        #Confirmação
        texto2 = f'''\nSegue abaixo a solicitação:
        
        Tipo do apartamento: Tipo {tipo};
        Quantia de pessoas: {pessoas} pessoas;
        Dias de estadia: {dias} dias;
        Valor total: R${total:.2f}.'''

        print(texto2)

        confirmacao = input('\nDeseja confirmar a reserva? (s/n): ').lower()
        
        if confirmacao == 's':
            break
        else:
            print('Preencha os dados novamente.')

    #Dados do cliente
    nome = input('\nDigite o seu nome: ')
    sobrenome = input('Digite o seu sobrenome: ')
    email = input('Digite o seu e-mail: ').lower()

    #Recibo final
    recibo = f'''
    Nome: {nome} {sobrenome}
    E-mail: {email}
    Tipo do apartamento: Tipo {tipo}
    Quantia de pessoas: {pessoas} pessoas
    Dias de estadia: {dias} dias
    Valor total: R${total:.2f}
        
    Os dados da sua compra foram enviados para o seu e-mail.
        
    Muito obrigado e volte sempre!
    '''

    print('\n'+'='*60)
    print()
    print(' '*25, 'RECIBO', ' '*25)
    print()
    print('='*60)
    print()
    print(recibo)

    finalizacao = input('Deseja realizar uma nova compra? (s/n): ').lower()

    if finalizacao == 's':
        print('\nIniciando nova compra...\n')
    else:
        break
