# Aula 10 - Exercício 31 - Custo da Viagem
# Italo Andrade Costa
# 24/10/2026

dis = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dis}Km.')
pas = dis * 0.45 if dis > 200 else dis * 0.50
print(f'E o preco da sua passagem será de R${pas:.2f}')
