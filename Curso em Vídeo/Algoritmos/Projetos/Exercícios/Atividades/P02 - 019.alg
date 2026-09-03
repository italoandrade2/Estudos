// Passo 02 - Condições Básicas (Atividade 19)
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Condições Básicas 19"

var
    nome: Caractere
    nota1, nota2: Inteiro
    media: Real
inicio
    Escreva ("Digite o nome do aluno: ")
    Leia (nome)
    Escreva ("Digite a primeira nota: ")
    Leia (nota1)
    Escreva ("Digite a segunda nota: ")
    Leia (nota2)

    media := (nota1 + nota2)/2

    Se (media >= 7) então
        Escreva ("O aluno ", nome, " foi aprovado.")
    senão
        Escreva ("O aluno ", nome, " foi reprovado.")
    FimSe
fimalgoritmo