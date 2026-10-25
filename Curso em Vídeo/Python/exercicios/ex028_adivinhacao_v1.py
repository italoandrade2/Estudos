# Aula 10 - Exercício 28 - Jogo da Adivinhação v.1.0
# Italo Andrade Costa
# 24/10/2026

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

num1 = int(input('Em que número eu pensei? '))
num2 = randint(0, 5)

print('PROCESSANDO...')
sleep(3)

if num1 == num2:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {num2} e não no {num1}!')
