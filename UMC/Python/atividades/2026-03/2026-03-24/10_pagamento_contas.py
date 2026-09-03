# Pagamento de Contas
# Nome: Italo Andrade Costa
# 24/03/2026 - Versão 1.0

salario = float(input('Digite o salário: R$'))
conta1 = float(input('Digite o valor da primeira conta: R$'))
conta2 = float(input('Digite o valor da segunda conta: R$'))

juros1 = conta1*(1+(2/100))
juros2 = conta2*(1+(2/100))

valor = salario-juros1-juros2

texto = f'''Salário: R${salario:.2f}
Primeira conta: R${conta1:.2f}
Segunda conta: R${conta2:.2f}
Primeira conta com juros: R${juros1:.2f}
Segunda conta com juros: R${juros2:.2f}
Valor restante: R${valor:.2f}'''

print(texto)