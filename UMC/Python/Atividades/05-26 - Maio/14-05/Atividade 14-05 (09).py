# Dicionário - Atividade 09
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

agenda = {
    'Ana': '9999-0001',
    'Carlos': '9999-0002',
    'Beatriz': '9999-0003',
    'Eduardo': '9999-0004',
    'Sérgio': '9999-0005'
}

nome = input('Digite um nome: ')

if nome in agenda:
    print(nome+':', agenda[nome])
else:
    tel = input('Nome não encontrado. Digite um telefone para adicionar: ')
    agenda[nome] = tel
    print(nome+':', agenda[nome])