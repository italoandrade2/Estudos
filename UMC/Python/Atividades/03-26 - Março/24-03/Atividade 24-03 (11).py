# Cálculo de Iluminação
# Nome: Italo Andrade Costa
# 24/03/2026 - Versão 1.0

larg = int(input('Digite a largura do cômodo: '))
alt = int(input('Digite a altura do cômodo: '))
area = larg*alt
pot = area*18

texto = f'''O cômodo possui {larg} de largura;
O cômodo possui {alt} de altura;
A área do cômodo é de {area} metros quadrados;
A potência de iluminação utilizada por esse cômodo será de {pot}W.'''

print(texto)