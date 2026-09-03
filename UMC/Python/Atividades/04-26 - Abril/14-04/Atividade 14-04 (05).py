# Validação de Desconto
# Nome: Italo Andrade Costa
# 14/04/2026 - Versão 1.0

idade = int(input('Digite a idade do cliente: '))

if idade <= 16 or idade >= 60:
    print('O cliente possui direito a desconto.')
else:
    print('O cliente não possui direito a desconto.')