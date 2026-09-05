// Aula 14 - Prática 2 - Listagem da Turma
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Listagem da Turma"
var
    nome: vetor[1..4] de Caractere
    n1: vetor[1..4] de Real
    n2: vetor[1..4] de Real
    media: vetor[1..4] de Real
    sm, mt: Real
    c, total: Inteiro
inicio
    Para c := 1 até 4 faça
        EscrevaL ("ALUNO", c)
        Escreva ("Nome: ")
        Leia (nome[c])
        Escreva ("Primeira nota: ")
        Leia (n1[c])
        Escreva ("Segunda nota: ")
        Leia (n2[c])
        media[c] := (n1[c] + n2[c])/2
        sm := sm + media[c]
    FimPara

    mt := sm / 4

    LimpaTela
    EscrevaL ("LISTAGEM DE ALUNOS")
    EscrevaL ("-----------------------")
    Para c := 1 até 4 faça
        EscrevaL (nome[c]:15, media[c]:4:1)
        Se (media[c] > mt) então
            total := total + 1
        FimSe
    FimPara

    EscrevaL ("Ao todo temos", total, " alunos acima da média da turma que é", mt:4:1)
fimalgoritmo