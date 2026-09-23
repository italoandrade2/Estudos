# Aula 07 - Exercício 8 - Conversor de Medidas
# Italo Andrade Costa
# 21/09/2026

m = float(input('Uma distância em metros: '))

print(f'A medida de {m:.1f}m corresponde a: ')
print(f'{m / 1000:.1f}km')
print(f'{m / 100:.1f}hm')
print(f'{m / 10:.1f}dam')
print(f'{m * 10:.0f}dm')
print(f'{m * 100:.0f}cm')
print(f'{m * 1000:.0f}mm')
