# Acesso por índice e startswith
# Nome: Italo Andrade Costa
# 08/06/2026 - Versão 1.0

Minha_Lista = ["Ana","Carlos","Beatriz","Eduardo","Sérgio"]

print(f'O nome {Minha_Lista[3]} começa com a letra "E"?')

if Minha_Lista[3].startswith("E"):
    print("Resposta: Sim")
else:
    print("Resposta: Não")