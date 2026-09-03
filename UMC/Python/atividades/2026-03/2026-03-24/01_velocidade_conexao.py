# Velocidade de Conexão
# Nome: Italo Andrade Costa
# 24/03/2026 - Versão 1.0

tam = float(input('Digite o tamanho do arquivo (bits): '))
vel = float(input('Digite a velocidade da conexão (bits/s): '))
tem = int(tam/vel)
print(f'O tempo para baixar o arquivo é de {tem} segundos.')