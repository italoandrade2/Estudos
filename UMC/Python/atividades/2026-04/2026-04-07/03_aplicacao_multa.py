# Aplicação de Multa
# Nome: Italo Andrade Costa
# 08/04/2026 - Versão 1.0
 
vel = int(input('Qual a velocidade do veículo?: '))
esc = input('Foi em área escolar (s/n)?: ').lower()
chuv = input('Estava chovendo (s/n)?: ').lower()

if chuv == 's':
    limite = 60
else:
    limite = 80

if vel > limite:
    excesso = vel-limite
    multa = excesso*7

    if esc == 's':
        multa*2

    print(f'Você foi multado. O valor da multa é de R${multa:.2f}')
else:
    print('Você não foi multado.')