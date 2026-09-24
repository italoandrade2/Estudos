# Aula 08 - Desafio 18 - Seno, Cosseno e Tangente
# Italo Andrade Costa
# 23/09/2026

from math import radians, sin, cos, tan

ang = int(input('Digite um ângulo: '))

rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'Um ângulo de {ang}º possui os valores de seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}.')
