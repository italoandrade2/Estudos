# Aula 07 - Exercício 15 - Aluguel de Carros
# Italo Andrade Costa
# 22/09/2026

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${total:.2f}')
