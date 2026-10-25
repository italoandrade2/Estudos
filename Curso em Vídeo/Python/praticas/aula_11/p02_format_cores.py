# Aula 11 - Prática 2 - Format com Cores
# Italo Andrade Costa
# 25/10/2026

a = 3
b = 5
print(f'\033[32m{a}\033[m e \033[31m{b}\033[m!!!')

nome = 'Italo'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))