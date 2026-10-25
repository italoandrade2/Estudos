# Aula 09 - Desafio 35 - Triângulo
# Italo Andrade Costa
# 24/10/2026

l1 = int(input('Digite o 1º comprimento: '))
l2 = int(input('Digite o 2º comprimento: '))
l3 = int(input('Digite o 3º comprimento: '))

if (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2:
    print(f'Os comprimentos formam um triângulo')
else:
    print(f'Os comprimentos não formam um triângulo.')
    