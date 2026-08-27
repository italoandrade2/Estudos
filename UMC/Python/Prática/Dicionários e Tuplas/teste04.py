import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

L1 = {
    111:['Luiz',15000],
    112:['Fulano',14500],
    113:['Sicrano',11000],
    114:['Beltrano',13000]
}

for chave, dados in L1.items():
    print(f'{chave:^10} {dados[0]:^10} R${dados[1]:^10.2f}')