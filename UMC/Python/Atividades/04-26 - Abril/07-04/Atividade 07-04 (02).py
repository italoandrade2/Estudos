# Aprovação de Empréstimo
# Nome: Italo Andrade Costa
# 08/04/2026 - Versão 1.0

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite a quantia de anos a pagar: '))
score = int(input('Digite o seu score: '))

meses = anos*12
prest = casa/meses

if score < 300:
    print('Empréstimo Negado. Score muito baixo.')
else:
    if score > 700:
        perc = 0.35
    else:
        perc = 0.30
        
    limite = salario*perc
    
    print (f'Prestação: R${prest:.2f}')
    
    if prest <= limite:
        print('Empréstimo Aprovado.')
    else:
        print('Empréstimo Negado. Prestação alta.')
