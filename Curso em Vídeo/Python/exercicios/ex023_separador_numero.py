# Aula 09 - Exercício 23 - Separando dígitos de um número
# Italo Andrade Costa
# 24/10/2026

num = int(input('Informe um número: '))

print(f'Analisando o número {num}')
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
