# Atualização usando update()
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

agenda = {
    'Ana': '9999-0001',
    'Carlos': '9999-0002',
    'Beatriz': '9999-0003',
    'Eduardo': '9999-0004',
    'Sérgio': '9999-0005'
}

agenda.update({'Lucas': '9999-0006'})

for i in agenda:
    print(i+':', agenda[i])