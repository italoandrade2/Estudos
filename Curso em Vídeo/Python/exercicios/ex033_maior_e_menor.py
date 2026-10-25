# Aula 10 - Exercício 33 - Maior e menor valores
# Italo Andrade Costa
# 24/10/2026

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 < n2 and n1 < n3:
    print(f'O menor valor digitado foi {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor valor digitado foi {n2}')
else:
    print(f'O menor valor digitado foi {n3}')

if n1 > n2 and n1 > n3:
    print(f'O maior valor digitado foi {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior valor digitado foi {n2}')
else:
    print(f'O maior valor digitado foi {n3}')
    