# Sistema de login
# Nome: Italo Andrade Costa
# 10/03/2026 - Versão 1.0

while True:
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if email == "aluno@umc.com" and senha == "aluno123":
        print("Bem vindo ao sistema!")
        break

    else:
        print("Dados incorretos. Tente novamente.")