// Aula 15 - Prática 4 - Preencher Matriz 4º ordem
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Preencher Matriz 4º ordem"
var
    mID: vetor[1..4, 1..4] de Inteiro
    i, j, soma, mult, maior3: Inteiro
inicio
    soma := 0
    mult := 1
    maior3 := 0

    Para i := 1 até 4 faça
        Para j := 1 até 4 faça
            Escreva ("Digite o valor da posição [", i, ",", j, "]")
            Leia (mID[i,j])

            Se (i = j) então
                soma := soma + mID[i,j]
            FimSe

            Se (i = 2) então
                mult := mult * mID[i,j]
            FimSe

            Se (mID[i,3] > maior3) então
                maior3 := mID[i,3]
            FimSe
        FimPara
    FimPara

    Para i := 1 até 4 faça
        Para j := 1 até 4 faça
            Escreva (mID[i,j]:3)
        FimPara
        EscrevaL ()
    FimPara

    EscrevaL ("A soma da diagonal principal é igual a", soma, ".")
    EscrevaL ("O produto da segunda linha é igual a", mult, ".")
    EscrevaL ("O maior valor da terceira coluna é igual a", maior3, ".")
fimalgoritmo