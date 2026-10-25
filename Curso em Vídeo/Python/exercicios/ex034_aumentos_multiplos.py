# Aula 10 - Exercício 34 - Aumentos múltiplos
# Italo Andrade Costa
# 24/10/2026

sal = float(input('Qual é o salário do funcionário: R$'))

nsal = sal * 1.10 if sal > 1250 else sal * 1.15

print(f'Quem ganhava R${sal:.2f} passa a ganhar R${nsal:.2f} agora.')
