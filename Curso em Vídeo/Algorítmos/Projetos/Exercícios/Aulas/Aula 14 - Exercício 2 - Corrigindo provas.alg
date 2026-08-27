// Aula 14 - Exercício 2 - Corrigindo provas
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Corrigindo provas"
var
    gabarito: vetor[1..5] de Caractere
    nome: vetor[1..3] de Caractere
    resp: vetor[1..5] de Caractere
    acertos: vetor[1..5] de Real
    total, media: Real
    i, j: Inteiro
Procedimento Aluno(x: Inteiro)
inicio
    EscrevaL ("----------------------------")
    EscrevaL ("ALUNO", x)
    EscrevaL ("----------------------------")
FimProcedimento
inicio
    EscrevaL ("PASSO 1 - Cadastro de Gabarito")
    EscrevaL ("-------------------------------")
    Para i := 1 até 5 faça
        Escreva ("Questão", i, ": ")
        Leia (gabarito[i])
    FimPara

    LimpaTela
    Para j := 1 até 3 faça
        Aluno(j)
        Escreva ("Nome: ")
        Leia (nome[j])
        EscrevaL ("RESPOSTAS DADAS")
        Para i := 1 até 5 faça
            Escreva ("Questão", i, ": ")
            Leia (resp[i])

            Se (resp[i] = gabarito[i]) então
                acertos[j] := acertos[j] + 2
            FimSe
        FimPara
        LimpaTela
    FimPara

    total := 0

    LimpaTela
    EscrevaL ("NOTAS FINAIS")
    EscrevaL ("-------------------------------")
    Para j := 1 até 3 faça
        EscrevaL (nome[j]:11, acertos[j]:2:1)
        total := total + acertos[j]
    FimPara
    EscrevaL ("-------------------------------")

    media := total / 3
    EscrevaL ("Média da Turma: ", media:2:1)
fimalgoritmo