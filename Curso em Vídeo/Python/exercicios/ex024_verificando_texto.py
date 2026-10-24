# Aula 09 - Exercício 24 - Verificando as primeiras letras de um texto
# Italo Andrade Costa
# 24/10/2026

cid = input('Em que cidade você nasceu? ').title()

sep = cid.split()

print("Santo" in (sep[0]))
