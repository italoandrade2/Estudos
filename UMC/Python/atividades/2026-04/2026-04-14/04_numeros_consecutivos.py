# Números Consecutivos
# Nome: Italo Andrade Costa
# 14/04/2026 - Versão 1.0

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n2 == (n1+1) and n3 == (n2+1):
    print('Os três números são sequenciais em ordem crescente.')
else:
    print('Os três números não são sequenciais.')