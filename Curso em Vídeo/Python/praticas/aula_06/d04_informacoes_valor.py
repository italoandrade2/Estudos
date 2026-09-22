# Aula 06 - Desafio 4 - Informações de Valores
# Italo Andrade Costa
# 19/09/2026

carac = input('Digite um valor: ')

print(type(carac))
print(f'São caracteres? {carac.isalpha()}')
print(f'São números? {carac.isnumeric()}')
print(f'São números e caracteres? {carac.isalnum()}')
print(f'Está em maíscula? {carac.isupper()}')
print(f'Está em minúscula? {carac.islower()}')
print(f'Está maiusculizado? {carac.istitle()}')
print(f'É espaço? {carac.isspace()}')
