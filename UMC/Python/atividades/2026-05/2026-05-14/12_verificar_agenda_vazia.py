# Verificar se a agenda está vazia
# Nome: Italo Andrade Costa
# 14/05/2026 - Versão 1.0

agenda = {
    'Ana': '9999-0001',
    'Carlos': '9999-0002',
    'Beatriz': '9999-0003',
    'Eduardo': '9999-0004',
    'Sérgio': '9999-0005'
}

contador = 0

for nome in agenda:
    contador += 1
    
if contador > 1:
    print(agenda)
else:
        print('Agenda vazia')