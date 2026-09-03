# Criar um dicionário a partir de duas listas
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

nome = ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']

tel = ['9999-0001', '9999-0002', '9999-0003', '9999-0004', '9999-0005',]

contatos = {}

for i in range(len(nome)):
    contatos[nome[i]] = tel[i]

print(contatos)