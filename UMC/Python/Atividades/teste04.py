# Controle de Notas
# Nome: Italo Andrade Costa
# 09/06/2026 - Versão 1.0

notas = []

total_notas = 0
aprovados = 0

for i in range(1,6):
    nota = float(input(f'Digite a nota do {i}º aluno: '))
    notas.append(nota)

    total_notas += nota

    if nota >= 6:
        aprovados += 1

media = total_notas / len(notas)

print(f'Média da turma: {media}')
print(f'Maior nota: {max(notas)}')
print(f'Menor nota: {min(notas)}')
print(f'Alunos aprovados: {aprovados}')