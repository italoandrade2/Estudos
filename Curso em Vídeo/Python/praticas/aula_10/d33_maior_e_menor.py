# Aula 09 - Desafio 33 - Maior e Menor
# Italo Andrade Costa
# 24/10/2026

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}.')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}.')
else:
    print(f'O maior número é {n3}.')

if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
else:
    print(f'O menor número é {n3}')
    