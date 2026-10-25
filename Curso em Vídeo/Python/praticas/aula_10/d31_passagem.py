# Aula 09 - Desafio 31 - Velocidade de um Carro
# Italo Andrade Costa
# 24/10/2026

km = int(input('Digite a distância da viagem em KMs: '))

if km <= 200:
    pas = km * 0.5
    print(f'A passagem é R$0.50 e o total é igual a R${pas:.2f}.')
else:
    pas = km * 0.45
    print(f'A passagem é R$0.45 e o total é igual a R${pas:.2f}.')
    