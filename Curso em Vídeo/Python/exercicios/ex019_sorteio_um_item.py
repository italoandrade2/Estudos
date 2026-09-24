# Aula 08 - Exercício 19 - Sorteando um item na lista
# Italo Andrade Costa
# 23/09/2026

from random import choice

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')

sort = choice([al1, al2, al3, al4])

print(f'O aluno escolhido foi {sort}')
