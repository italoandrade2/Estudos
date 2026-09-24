# Aula 08 - Exercício 18 - Seno, Cosseno e Tangente
# Italo Andrade Costa
# 23/09/2026

from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo que você dejesa: '))

rad = radians(ang)

print(f'O ângulo de {ang} tem o SENO de {sin(rad):.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cos(rad):.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan(rad):.2f}')
