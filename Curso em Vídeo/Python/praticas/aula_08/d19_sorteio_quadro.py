# Aula 08 - Desafio 19 - Sorteio de Aluno
# Italo Andrade Costa
# 23/09/2026

from random import choice

al1 = input('Digite o nome do 1º aluno: ')
al2 = input('Digite o nome do 2º aluno: ')
al3 = input('Digite o nome do 3º aluno: ')
al4 = input('Digite o nome do 4º aluno: ')

sort = choice([al1, al2, al3, al4])

print(f'O aluno sorteado para apagar o quadro foi {sort}.')
