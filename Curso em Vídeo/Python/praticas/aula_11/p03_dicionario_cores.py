# Aula 11 - Prática 3 - Dicionário de Cores
# Italo Andrade Costa
# 25/10/2026

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

nome = 'Italo'
print(f'Olá, muito prazer em te conhecer, {cores['pretoebranco']}{nome}{cores['limpa']}!!!')
