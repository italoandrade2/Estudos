# Validação usando 'método' com Loop
# Nome: Italo Andrade Costa
# 17/03/2026 - Versão 1.0

COR = '\033[1;32;40m'
FIM_COR = '\033[0m'

while True:
    v1 = input("Entre com o Primeiro Valor, deve ser um número inteiro: ")
    v2 = input("Entre com o Segundo Valor, deve ser um número inteiro: ")
    if v1.isdigit() and v2.isdigit() and v2 != "0":
        v1 = int(v1)
        v2 = int(v2)
        break
    else:
        print(f"Os dois valores devem ser inteiros e o "
              f"segundo valor diferente de 0, entre os dados novamente")

div = v1 / v2

print   (f"O resultado da divisão é"
                f"{COR} {div:.2} {FIM_COR}")