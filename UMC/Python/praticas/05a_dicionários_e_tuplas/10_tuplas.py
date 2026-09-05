# Tuplas
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

import os

L1 = ('Luiz','Fulano','Sicrano','Beltrano')

for i in L1:
    print(f'{i:>10}')
print(f'{'=':=^10}')
print(f'{L1[1]:>10}')
print(f'{'=':=^10}')
L1[1]='Não Pode'