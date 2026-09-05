// Aula 15 - Prática 1 - Matriz 3x2
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Matriz 3x2"
var
    mat: vetor[1..3, 1..2] de Inteiro
    l, c: Inteiro
inicio
    Para l := 1 até 3 faça
        Para c := 1 até 2 faça
            Escreva ("Digite o valor da posição [", l, ",", c, "]: ")
            Leia (mat[l, c])
        FimPara
    FimPara

    Para l := 1 até 3 faça
        Para c := 1 até 2 faça
            Escreva (mat[l, c]:5)
        FimPara
        EscrevaL ()
    FimPara
fimalgoritmo