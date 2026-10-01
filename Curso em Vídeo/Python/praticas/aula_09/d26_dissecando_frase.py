# Aula 09 - Desafio 26 - Dissecando uma Frase
# Italo Andrade Costa
# 25/06/2026

frase = input('Digite uma frase: ')

print(f'A letra "a" aparece {frase.count('a')} vezes.')
print(f'A letra "a" aparece pela primeira vez na {frase.find('a')}º posição.')
print(f'A letra "a" aparece pela última vez na {frase.rfind('a')}º posição.')
