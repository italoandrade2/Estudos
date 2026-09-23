# Aula 07 - Exercício 12 - Calculando Descontos
# Italo Andrade Costa
# 22/09/2026

valor = float(input('Qual é o preço do produto? R$'))
desconto = valor * (1 - 0.05)

print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custar R${desconto:.2f}')
