# Aula 08 - Exercício 17 - Catetos e Hipotenusa
# Italo Andrade Costa
# 23/09/2026

from math import sqrt, pow

cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))

hip = sqrt(pow(cat1, 2) + pow(cat2, 2))

print(f'A hipotenusa vai medir {hip:.2f}')
