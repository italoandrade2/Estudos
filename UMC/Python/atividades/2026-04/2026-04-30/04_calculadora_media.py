# Calculadora de Médias com Lista
# Nome: Italo Andrade Costa
# 04/05/2026 - Versão 1.0

notas = []
apro = 0

for i in range(5):
    n = float(input(f'Digite o {i+1}º número: '))
    notas.append(n)

    if n >= 6.0:
        apro += 1

mediat = sum(notas)/5


texto = f'''
A média total da sala é de {mediat};
A maior nota é {max(notas)};
A menor nota é {min(notas)};
A quantia de alunos aprovados é de {apro}.'''

print(texto)
