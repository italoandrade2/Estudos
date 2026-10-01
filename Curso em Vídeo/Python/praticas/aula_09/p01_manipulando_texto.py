# Aula 09 - Prática 1 - Manipulando Texto
# Italo Andrade Costa
# 25/09/2026

frase = "Curso em Vídeo Python"

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1::2])

print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

lista = frase.split()
print(lista)
print(lista[0])

print('-'.join(lista))

frase2 = "   Aprenda Python  "

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

print('''Python é uma linguagem de programação de alto nível, interpretada de script,
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por
Guido van Rossum em 1991. Atualmente, possui um modelo de desenvolvimento
comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software
Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações
formais, a linguagem, como um todo, não é formalmente especificada. O padrão na
pratica é a implementação CPython.''')