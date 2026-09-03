# Conversão de Segundos
# Nome: Italo Andrade Costa
# 24/03/2026 - Versão 1.0

seg1 = int(input('Digite os segundos: '))
min = int(seg1/60)
seg2 = int(seg1%60)

print(f'{seg1} segundos equivalem a {min} minutos e {seg2} segundos.')