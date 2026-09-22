# Aula 06 - Exercício 4 - Informações de um Valor
# Italo Andrade Costa
# 19/09/2026

valor = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(valor)}')
print(f'Só tem espaços? {valor.isspace()}')
print(f'É um número: {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está capitalizada? {valor.istitle()}')
