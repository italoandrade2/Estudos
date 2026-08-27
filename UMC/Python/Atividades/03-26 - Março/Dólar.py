# Conversão de Dólar para Real
# Nome: Italo Andrade Costa
# 05/03/2026 - Versão 1.0
 
num1 = float(input("Digite o valor a ser convertido: "))
dolar = 5.23

texto = f"""A conversão do valor inserido é:

Valor Inserido: R${num1}
Valor do dólar: R$5.23
Valor final: ${float(num1 / dolar)}
"""

print(texto)