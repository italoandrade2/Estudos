# Função Get
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

import os
os.system('cls')

agenda = {'Ana': '9999-0001', 'Carlos': '9999-0002'}

print(agenda.get('Ana','Nome não encontrado'))

print(agenda.get('Beatriz','Nome não encontrado'))