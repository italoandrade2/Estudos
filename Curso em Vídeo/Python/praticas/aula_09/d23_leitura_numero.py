# Aula 09 - Desafio 22 - Dissecando um Nome
# Italo Andrade Costa
# 25/06/2026

num = input('Digite um número entre 0 a 9999: ')

sep = ('-'.join(num)).split('-')

print(f"Unidade: {sep[3]}")
print(f"Dezena: {sep[2]}")
print(f"Centena: {sep[1]}")
print(f"Milhar: {sep[0]}")
