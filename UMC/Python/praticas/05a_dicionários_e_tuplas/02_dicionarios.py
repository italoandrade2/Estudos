# Dicionários 2
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

import os
os.system('cls')

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

L1 = {
    'Luiz':15000,
    'Fulano':14500,
    'Sicrano':11000,
    'Beltrano':13000
}

del L1['Luiz']
L1['Fulano'] = 10000

for i in L1:
    salario = locale.currency(L1[i], grouping=True, symbol=True)
    print(f'{i:15} {salario:<10}')