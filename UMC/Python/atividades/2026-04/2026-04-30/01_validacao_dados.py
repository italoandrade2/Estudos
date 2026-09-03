# Validação de Dados Pessoais
# Nome: Italo Andrade Costa
# 04/05/2026 - Versão 1.0

nome = input('Digite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))
alt = float(input('Digite a altura do aluno: '))

if nome and 16 <= idade <= 60 and 1.0 <= alt <= 2.5:
    print('O aluno está matriculado.')
else:
    print('O aluno não foi encontrado.')
