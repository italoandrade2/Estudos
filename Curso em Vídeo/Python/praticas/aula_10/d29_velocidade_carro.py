# Aula 09 - Desafio 29 - Velocidade de um Carro
# Italo Andrade Costa
# 24/10/2026

vel = int(input('Digite a velocidade percorrida em KMs: '))

if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você ultrapasssou o limite de velocidade em {vel - 80}km. Receberá uma multa de R${multa:.2f}.')
else:
    print('Você não ultrapassou o limite de velocidade.')
    