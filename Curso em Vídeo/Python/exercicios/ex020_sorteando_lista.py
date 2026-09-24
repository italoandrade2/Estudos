# Aula 08 - Exercício 20 - Sorteando uma ordem na lista
# Italo Andrade Costa
# 23/09/2026

from random import shuffle

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')

alunos = [al1, al2, al3, al4]

shuffle(alunos)

print(f'A ordem de apresentação será\n{alunos}')
