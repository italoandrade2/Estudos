# Aula 09 - Desafio 34 - Aumento Salarial
# Italo Andrade Costa
# 24/10/2026

sal = float(input('Digite o salário R$'))

if sal > 1250.00:
    saln = sal * (1+0.10)
    print(f'O salário de R${sal:.2f} com um aumento de 10% é igual a R${saln:.2f}')
else:
    saln = sal * (1+0.15)
    print(f'O salário de R${sal:.2f} com um aumento de 15% é igual a R${saln:.2f}')
    