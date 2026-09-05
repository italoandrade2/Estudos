# Usando If xx in 2
# Nome: Italo Andrade Costa
# 05/05/2026 - Versão 1.0

from datetime import datetime
agora = datetime.now()
L1=[]
a=0
L1=list(range(10,20,2))
for i in L1:
    print(f" Posição da Lista {a} ==== Valor = {i}")
    a+=1
if 30 not in L1:
    print(' 30 não está na lista')
print(f"{'='*40}")
print(f'Programa executado em {agora:%Y-%m-%d %H:%M}')