# Cálculo de Salário
# Nome: Italo Andrade Costa
# 24/03/2026 - Versão 1.0

horas = int(input('Digite a quantia de horas trabalhadas: '))
salmin = 1621.00
horatrab = salmin/2
salbrut = horatrab*horas
imp = salbrut*(3/100)
salfinal = salbrut-imp

texto = f'''Valor do salário mínimo: R${salmin};
Valor da hora trabalhada: R${horatrab:.2f};
Quantia de horas trabalhadas: {horas} horas;
Salário bruto: R${salbrut:.2f};
Valor do imposto: R${imp:.2f};
Salário Líquido: R${salfinal:.2f}.'''

print(texto)