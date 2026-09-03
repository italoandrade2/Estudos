# Divisão de Números
# Nome: Italo Andrade Costa
# 14/04/2026 - Versão 1.0

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num2 == 0:
    print('Erro! Impossível dividir por zero.')
else:
    div = num1 / num2
    print(f'{num1} dividido por {num2} é igual a {div}.')