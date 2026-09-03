# Cálculo de Idade
# Nome: Italo Andrade Costa
# 24/03/2026 - Versão 1.0

ano1 = int(input('Digite seu ano de nascimento: '))
ano2 = int(input('Digite o ano atual: '))
atual = ano2-ano1
fut = 2030-ano1

texto = f'''Você atualmente tem {atual} anos;
Em 2030, você terá {fut} anos.'''

print(texto)