# Aula 08 - Desafio 17 - Triângulo Retângulo
# Italo Andrade Costa
# 23/09/2026

from math import sqrt, pow

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjac = float(input('Digite o comprimento do cateto adjacente: '))

hipot = sqrt((pow(oposto, 2)) + (pow(adjac, 2)))

print(f'A hipotenusa de um triângulo retângulo de catetos {oposto:.2f}cm e {adjac:.2f}cm é igual a {hipot:.2f}cm')
