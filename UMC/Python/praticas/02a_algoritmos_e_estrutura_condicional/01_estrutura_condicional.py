# Estrutura Condicional
# Nome: Italo Andrade Costa
# 10/03/2026 - Versão 1.0

primeiro_numero = int(input("Entre com o primeiro valor: "))
segundo_numero = int(input("Entre com o segundo valor: "))

if primeiro_numero > segundo_numero:
    print("O maior número é:", primeiro_numero)
elif segundo_numero > primeiro_numero:
    print("O maior número é:", segundo_numero)
else:
    print("Os dois números são iguais:", segundo_numero)

print("Acabou a comparação.")