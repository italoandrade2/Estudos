// Aula 09 - Exercício 2 - Melhor aluno da turma
// Nome: Italo Andrade Costa
// 28/05/2026 - Versão 1.0

algoritmo "Melhor aluno da turma"
var
   alunos, contador: Inteiro
   nota, notam: real
   nome, nomem: Caractere
inicio
    EscrevaL ("------------------------")
    EscrevaL (" Escola Santa Paciência ")
    EscrevaL ("------------------------")

    Escreva ("Quantos alunos a turma tem? ")
    Leia (alunos)

    contador <- 1
    notam <- 0

    Enquanto (contador <= alunos) faca
        EscrevaL ("---------------")
        EscrevaL ("ALUNO", contador)
        Escreva ("Nome do aluno: ")
        Leia (nome)
        Escreva ("Nota de ", nome, ": ")
        Leia (nota)

        Se (nota > notam) entao
            notam <- nota
            nomem <- nome
        FimSe

        contador <- contador + 1
    FimEnquanto

    EscrevaL ("-------------------")
    EscrevaL ("O melhor aproveitamento foi de ", nomem, " com a nota", notam)
fimalgoritmo