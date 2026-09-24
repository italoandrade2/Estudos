# Aula 08 - Desafio 20 - Sorteio de Apresentação
# Italo Andrade Costa
# 23/09/2026

from random import sample

al1 = input('Digite o nome do 1º aluno: ')
al2 = input('Digite o nome do 2º aluno: ')
al3 = input('Digite o nome do 3º aluno: ')
al4 = input('Digite o nome do 4º aluno: ')

sort = sample([al1, al2, al3, al4], 4)

print('Os alunos farão a apresentação na seguinte ordem:')
print(f'1º - {sort[0]}')
print(f'2º - {sort[1]}')
print(f'3º - {sort[2]}')
print(f'4º - {sort[3]}')
