tam = float(input('Digite o tamanho do arquivo (bits): '))
vel = float(input('Digite a velocidade da conexão (bits/s): '))
tem = int(tam/vel)
print(f'O tempo para baixar o arquivo é de {tem} segundos.')