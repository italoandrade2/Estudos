# Try e Except com Loop
# Nome: Italo Andrade Costa
# 17/03/2026 - Versão 1.0

COR = '\033[1;32;40m'
FIM_COR = '\033[0m'

while True:
    try:
        v1 = int(input("Entre com o Primeiro Valor, deve ser um número inteiro: "))
    except ValueError as error:
        print("Valor Inválido, digite novamente")
    else:
        break
while True:
    try:
        v2 = int(input("Entre com o Segundo Valor, deve ser um número inteiro: "))
    except ValueError as error:
        print("Valor Inválido, digite novamente")
    else:
        break
div = v1 / v2

print   (f"O resultado da divisão é"
                f"{COR} {div:.2} {FIM_COR}")