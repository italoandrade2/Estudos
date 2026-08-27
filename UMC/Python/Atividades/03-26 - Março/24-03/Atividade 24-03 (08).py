pesokg = int(input('Digite o peso da ração em kg: '))
pesog = pesokg*1000

gato1 = int(input('Digite a quantia de ração consumida pelo 1º gato por dia em gramas: '))
gato2 = int(input('Digite a quantia de ração consumida pelo 2º gato por dia em gramas: '))
dia5 = pesog-(gato1+gato2)*5

texto = f'''Peso da ração em gramas: {pesog}g;
Quantia de ração consumida pelo 1º gato por dia: {gato1}g;
Quantia de ração consumida pelo 2º gato por dia: {gato2}g;
Ração restante após 5 dias: {dia5}g'''

print(texto)