# Aula 07 - Prática 1 - Operadores Aritméticos
# Italo Andrade Costa
# 19/09/2026

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

som = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divi = n1 // n2
exp = n1 ** n2

print(f'A soma vale {som}')
print(f'A subtração vale {sub}')
print(f'A multiplicação vale {mult}')
print(f'A divisão vale {div:.2f}')
print(f'A divisão inteira vale {divi}')
print(f'A potência vale {exp}')
