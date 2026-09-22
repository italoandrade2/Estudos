# Aula 07 - Desafio 11 - Área de Parede
# Italo Andrade Costa
# 21/09/2026

larg = float(input('Digite a largura da parede (m): '))
alt = float(input('Digite a altura da parede (m): '))

area = larg * alt
tinta = area / 2

print(f'Para pintar uma parede de {area}m², você deverá usar {tinta} litro(s) de tinta.')
