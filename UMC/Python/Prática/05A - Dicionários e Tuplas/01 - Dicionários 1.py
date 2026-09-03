# Dicionários 1
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

import os
os.system('cls')
Dict01 = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50
}

print(Dict01)

print(Dict01['Alface'])

print('Manga' in Dict01)
print('Batata' in Dict01)

print(Dict01.values())

for i in sorted(Dict01, reverse=True):
    print(i, Dict01[i])