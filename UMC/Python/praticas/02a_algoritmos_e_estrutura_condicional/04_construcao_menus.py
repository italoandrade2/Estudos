# Construção de Menus
# Nome: Italo Andrade Costa
# 10/03/2026 - Versão 1.0

import os
os.system('cls')

opt = input('''
Categoria       Preço R$
[1] Opção 01
[2] Opção 02
[3] Opção 03
Opção = ''')

if opt not in ["1", "2", "3"]:
    os.system('cls')
    print("OPÇÃO INVÁLIDA")
if opt == '1':
    os.system('cls')
    print("Opção 01 Selecionada")
if opt == '2':
    os.system('cls')
    print("Opção 02 Selecionada")
if opt == '3':
    os.system('cls')
    print("Opção 03 Selecionada")

print("Fim do Programa")
input("Digite Enter para Finalizar")