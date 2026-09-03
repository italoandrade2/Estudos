# Números Repetidos
# Nome: Italo Andrade Costa
# 14/04/2026 - Versão 1.0

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))

if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print('Há números repetidos.')
else:
    print('Não há números repetidos.')