# Enumerar elementos
# Nome: Italo Andrade Costa
# 08/06/2026 - Versão 1.0

Minha_Lista = ["Ana","Carlos","Beatriz","Eduardo","Sérgio"]

print('Posição de nomes com mais de 6 letras:')
for i, val in enumerate(Minha_Lista):
    if len(val) > 6:
        print(f' {i}º - {val}')