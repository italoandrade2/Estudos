import os

L1 = ('Luiz','Fulano','Sicrano','Beltrano')

for i in L1:
    print(f'{i:>10}')
print(f'{'=':=^10}')
print(f'{L1[1]:>10}')
print(f'{'=':=^10}')
L1[1]='Não Pode'