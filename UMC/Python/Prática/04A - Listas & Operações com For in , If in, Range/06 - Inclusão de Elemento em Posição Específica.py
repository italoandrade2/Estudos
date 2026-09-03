# Inclusão de Elemento em Posição Específica
# Nome: Italo Andrade Costa
# 05/05/2026 - Versão 1.0

import os
os.system("cls")
Minha_Lista=["Fulano","Eulano","Tulano","Sicrano","Beltrano"]
i=Minha_Lista.index("Sicrano")
Minha_Lista.insert(i+1,"Sicrano 2")
print("Lista Alterada\t",Minha_Lista)