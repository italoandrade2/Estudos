# Entrada
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

# Processamento
soma = v1 + v2
subtrai = v1 - v2
multiplica = v1 * v2
divide = v1 / v2
x,y = divmod(v1, v2)
w = pow (v1, v2)

# Saída
print(" A soma de %i com %i = %i" %(v1, v2, soma))
print(" A subtração de %i com %i = %i" %(v1, v2, subtrai))
print(" A multiplicação de %i com %i = %i" %(v1, v2, multiplica))
print(" A divisão de %i com %i = %i" %(v1, v2, divide))
print(" A parte inteira de %i dividido por %i é igual a %i e o resto da divisão é igual a %i" %(v1, v2, x,y))
print(" %i elevado a %i = %i" %(v1, v2, w))