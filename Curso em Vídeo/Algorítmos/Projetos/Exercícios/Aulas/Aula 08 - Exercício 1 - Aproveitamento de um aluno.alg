// Aula 08 - Exercício 1 - Aproveitamento de um aluno
// Nome: Italo Andrade Costa
// 26/05/2026 - Versão 1.0

algoritmo "Aproveitamento de um aluno"
var
    nota1, nota2, media: Real
    aproveitamento: Caractere
inicio
    EscrevaL ("-----------------------")
    EscrevaL (" ESCOLA JAVALI CANSADO ")
    EscrevaL ("-----------------------")
    Escreva ("Primeira Nota: ")
    Leia (nota1)
    Escreva ("Segunda Nota: ")
    Leia (nota2)

    EscrevaL ("-----------------------")

    media <- (nota1 + nota2) / 2

    EscrevaL (" MÉDIA:", media)
    Se (media < 5) entao
        EscrevaL (" APROVEITAMENTO: F")
    senao
        Se (media >= 5) e (media < 6) entao
            EscrevaL (" APROVEITAMENTO: E")
        senao
            Se (media >= 6) e (media < 7) entao
                EscrevaL (" APROVEITAMENTO: D")
            senao
                Se (media >= 7) e (media < 8) entao
                    EscrevaL (" APROVEITAMENTO: C")
                senao
                    Se (media >= 8) e (media < 9) entao
                        EscrevaL (" APROVEITAMENTO: B")
                    senao
                        EscrevaL (" APROVEITAMENTO: A")
                    FimSe
                FimSe
            FimSe
        FimSe
    FimSe
    EscrevaL("-----------------------")
fimalgoritmo