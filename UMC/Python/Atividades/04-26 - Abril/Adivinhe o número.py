# Adivinhe o número
# Nome: Italo Andrade Costa
# 08/04/2026 - Versão 1.0
 
while True:
    numero = int(input('Digite um número (0 a 15): '))

    if numero == 11:
        print('Parabéns! Você adivinhou!')
        break
    elif numero > 15:
        print('Erro. Digite apenas números entre 0 a 15.')
    else:
        print('Você errou. Tente novamente!')