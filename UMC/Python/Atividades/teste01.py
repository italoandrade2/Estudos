while True:
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    altura = float(input('Digite a altura do aluno: '))
    
    if nome and 16 <= idade <= 60 and 1.0 <= altura <= 2.5:
        print('Cadastro Válido:')
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Altura: {altura}')
        break
    else:
        print('Cadastro Inválido! Preencha novamente:')