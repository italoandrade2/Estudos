# Aula 09 - Desafio 28 - Adivinhe o número
# Italo Andrade Costa
# 24/10/2026

from random import randint

num1 = int(input('Escolha um número de 0 a 5: '))

num2 = randint(0, 5)

if num1 == num2:
    print('Parabéns! Você acertou o número!')
else:
    print(f'Que pena. O número certo era {num2}.')
    