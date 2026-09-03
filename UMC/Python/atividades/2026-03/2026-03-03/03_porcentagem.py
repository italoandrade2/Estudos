# Cálculo de Porcentagem
# Nome: Italo Andrade Costa
# 03/03/2026 - Versão 1.0

num1 = float(input("Digite o valor desejado: "))
porc = float(input("Digite a porcentagem: "))
desconto = num1*(porc/100)

texto = f"""A porcentagem do valor inserido é:

Valor inserido: {num1}
Porcentagem: {porc}%
Valor do desconto: {desconto}
Valor final: {num1-desconto}
"""

print(texto)