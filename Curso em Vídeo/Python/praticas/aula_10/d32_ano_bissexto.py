# Aula 09 - Desafio 32 - Ano Bissexto
# Italo Andrade Costa
# 24/10/2026

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é um ano Bissexto.')
        else:
            print(f'O ano {ano} não é um ano Bissexto.')
    else:
        print(f'O ano {ano} é um ano Bissexto.')
else:
    print(f'O ano {ano} não é um ano Bissexto.')
    