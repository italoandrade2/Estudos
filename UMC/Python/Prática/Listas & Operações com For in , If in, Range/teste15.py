Minha_Lista=[
    "Fulano da Silva","Eulano de Souza","Tulano Junior",
    "Sicrano da Silva","Voslano Fulano Junior"]
Nome=input("Entre com o nome a ser pesquisado: ")
for i in Minha_Lista:
    if Nome in i:
        print(i)
print("=======================")