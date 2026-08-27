# Acrescentar elemento
# Nome: Italo Andrade Costa
# 08/06/2026 - Versão 1.0

Minha_Lista = ["Ana","Carlos","Beatriz","Eduardo","Sérgio"]

nome = input('Digite um nome: ')

if nome in Minha_Lista:
    print("O nome já está na lista.")
else:
    Minha_Lista.append(nome)
    print("Nome adicionado com sucesso!")
    print(Minha_Lista)