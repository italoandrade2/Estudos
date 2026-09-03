# Tabuada com For
# Nome: Italo Andrade Costa
# 04/05/2026 - Versão 1.0

num = int(input('Digite um número: '))
soma = 0

for i in range(1, 11):
    tab = num*i
    soma += tab
    print(f'{num} x {i} = {tab}')

print(f'\nA soma de todos os resultados é {soma}')
