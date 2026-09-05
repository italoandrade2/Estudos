# Estrutura Condicional Aninhada
# Nome: Italo Andrade Costa
# 10/03/2026 - Versão 1.0

tabela = '''
Categoria       Preço R$
1               10,00
2               18,00
3               23,00
4               26,00'''

print(tabela, "\n")

categoria = int(input("Entre com a categoria do produto conforme a tabela: "))

if categoria == 1:
    preço = 10
else:
    if categoria == 2:
        preço = 18
    else:
        if categoria == 3:
            preço = 23
        else:
            if categoria == 4:
                preço = 26
            else:
                print("Categoria inválida, digite um valor entre 1 e 4")
                preço = 0

print("A categoria do produto é %i e seu preço é R$%.2f." %(categoria, preço))