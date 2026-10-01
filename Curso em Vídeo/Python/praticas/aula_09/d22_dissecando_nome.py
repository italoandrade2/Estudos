# Aula 09 - Desafio 22 - Dissecando um Nome
# Italo Andrade Costa
# 25/06/2026

nomec = input('Digite seu nome completo: ')

nome = nomec.split()

print(f'Seu nome em maísculo: {nomec.upper()}')
print(f'Seu nome em minúsculo: {nomec.lower()}')
print(f'O nome completo possui {len(nomec.replace(" ", ""))} letras')
print(f'O primeiro nome possui {len(nome[0])} letras')
