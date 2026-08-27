# Dicionário - Atividade 18
# Nome: Italo Andrade Costa
# 18/05/2026 - Versão 1.0

agenda = {
    'Ana': '9999-0001',
    'Carlos': '9999-0002',
    'Beatriz': '9999-0003',
    'Eduardo': '9999-0004',
    'Sérgio': '9999-0005'
}

agenda2 = {
    nome: numero
    for nome, numero in agenda.items()
    if numero.endswith(('1', '3', '5'))
}

for i in agenda2:
    print(i+':', agenda2[i])