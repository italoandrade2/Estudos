# Aula 09 - Exercício 22 - Analisador de Textos
# Italo Andrade Costa
# 24/10/2026

nome = input('Digite seu nome completo: ')
nome_sep = nome.split()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras')
print(f'Seu primeiro nome é {nome_sep[0]} e ele tem {len(nome_sep[0])} letras')
