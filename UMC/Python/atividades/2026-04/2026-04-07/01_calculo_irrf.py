# Cálculo de IRRF
# Nome: Italo Andrade Costa
# 08/04/2026 - Versão 1.0

sal = float(input('Digite o seu salário: R$'))

if sal <= 2428.80:
    ir = 0
elif sal <= 2826.65:
    ir = sal*0.075-182.16
elif sal <= 3751.05:
    ir = sal*0.15-394.16
elif sal <= 4664.68:
    ir = sal*0.225-675.49
else:
    ir = sal*0.275-908.73

print(f'Seu IRRF é de = R${ir:.2f}')