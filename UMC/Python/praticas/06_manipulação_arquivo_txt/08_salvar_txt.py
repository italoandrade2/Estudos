# Salvar uma lista como arquivo TXT
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

notas = [
    "Ana Silva - 9.5",
    "Bruno Oliveira - 7.0",
    "Carlos Mendes - 8.2",
    "Daniela Rocha - 9.8",
]

with open("notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(linha + "\n" for linha in notas)

print("notas.txt salvo!")