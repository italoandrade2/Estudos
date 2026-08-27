# Diário
# Nome: Italo Andrade Costa
# 28/05/2026 - Versão 1.0

from datetime import datetime

texto = '''=== MEU DIÁRIO ===
1. Nova entrada
2. Ler diário
3. Sair
4. Apagar todas as entradas'''

print(texto)

while True:
    escolha = int(input('\nEscolha: '))
    
    if escolha == 1:
        with open('diario.txt', 'a', encoding='utf-8') as arquivo:
            entrada = input('Escreva sua entrada: ')
            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            arquivo.write(f'[{data_hora}] {entrada}\n')
            print('Entrada salva!')
    elif escolha == 2:
        print('--- Diário ---')
        with open('diario.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            if linhas:
                for linha in linhas:
                    print(linha.strip())
            else:
                print('O diário está vazio.')
    elif escolha == 3:
        print('Programa finalizado!')
        break
    elif escolha == 4:
        confirmacao = input('Você tem certeza que deseja excluir tudo? (S/N) ').lower()

        if confirmacao == 's':
            with open('diario.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write('')
                print('Diário excluído!')
        else:
            print('Retornando...')