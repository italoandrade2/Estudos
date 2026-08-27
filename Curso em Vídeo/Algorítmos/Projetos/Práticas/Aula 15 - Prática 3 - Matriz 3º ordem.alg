// Aula 15 - Prática 3 - Matriz 3º ordem
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Matriz 3º ordem"
var
    mID: vetor[1..3, 1..3] de Inteiro
    i, j: Inteiro
inicio
    Para i := 1 até 3 faça
        Para j := 1 até 3 faça
            Se (i = j) então
                mID[i,j] := 1
            senão
                mID[i,j] := 0
            FimSe    
        FimPara
    FimPara

    Para i := 1 até 3 faça
        Para j := 1 até 3 faça
            Escreva (mID[i,j]:3)
        FimPara
        EscrevaL ()
    FimPara
fimalgoritmo