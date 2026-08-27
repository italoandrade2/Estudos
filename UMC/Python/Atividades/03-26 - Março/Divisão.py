# Cálculo de Divisão
# Nome: Italo Andrade Costa
# 05/03/2026 - Versão 1.0

num1 = float(input("Insira o valor a ser dividido: "))
num2 = float(input("Insira a quantia que irá dividir: "))

texto = f"""Os valores serão:

Valor Dividido: {num1}
Quantia dividida: {num2}
Resultado da divisão: {num1 / num2}
Divisão Inteira: {num1 // num2}
Resto da Divisão: {num1 % num2}
"""

print(texto)