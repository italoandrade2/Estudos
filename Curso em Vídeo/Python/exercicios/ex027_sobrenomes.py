# Aula 09 - Exercício 27 - Primeiro e último nome de uma pessoa
# Italo Andrade Costa
# 24/10/2026

nome = input('Digite seu nome completo: ').split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
