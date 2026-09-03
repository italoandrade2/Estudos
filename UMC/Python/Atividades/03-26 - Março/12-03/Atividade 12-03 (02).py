# Conversão de Moeda
# Nome: Italo Andrade Costa
# 12/03/2026 - Versão 1.0

real = float(input("Digite o valor desejado: R$"))
dolar = 5.25

texto = f"""Segue abaixo os valores solicitados:

Valor em reais: R${real:.2f}
Valor do dólar: R${dolar:.2f}
Valor convertido: ${real/dolar:.2f}
"""

print(texto)