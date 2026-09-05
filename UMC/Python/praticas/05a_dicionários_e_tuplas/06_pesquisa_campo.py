# Pesquisa por campo
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

import os
os.system('cls')

Dict1 = {
    111:['Luiz',15000],
    112:['Fulano',14500],
    113:['Sicrano',11000],
    114:['Beltrano',13000]
}

while True:
    val = int(input('Entre com a matrícula a ser pesquisada: '))
    if val in Dict1:
        print(val, Dict1[val])
    else:
        print('Matrícula não encontrada.')