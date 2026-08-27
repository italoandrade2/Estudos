import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
os.system('cls')

L1 = {
    111:['Luiz',15000],
    112:['Fulano',14500],
    113:['Sicrano',11000],
    114:['Beltrano',13000]
}

del L1[111]
L1[112][0] = 'Fulano da Silva'
L1[112][1] = 10000

for i in L1:
    salario = locale.currency(L1[i][1], grouping=True, symbol=True)
    print(f'{i:^15} {L1[i][0]:<20} {salario:<10}')