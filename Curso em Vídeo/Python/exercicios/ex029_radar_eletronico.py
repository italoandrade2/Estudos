# Aula 10 - Exercício 29 - Radar Eletrônico
# Italo Andrade Costa
# 24/10/2026

vel = float(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')

print('Tenha um bom dia! Dirija com segurança!')
