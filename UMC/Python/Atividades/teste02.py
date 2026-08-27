num = int(input('Digite o número para exibir a tabuada: '))

soma = 0

for i in range(1,11):
    res = num*i
    print(f'{num} x {i} = {res}')
    soma += res

print(f'\nA soma de todos os resultados é {soma}.')