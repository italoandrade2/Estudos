// Aula 14 - Prática 1 - Valores Pares
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Valores Pares"
var
    val: vetor[1..7] de Inteiro
    ind, totpar: Inteiro
inicio
    totpar := 0

    Para ind := 1 até 7 faça
        Escreva ("Digite o", ind, "º valor: ")
        Leia (val[ind])
    FimPara

    Para ind := 1 até 7 faça
        Se (val[ind] % 2 = 0) então
            totpar := totpar + 1
            EscrevaL ("Valor PAR na Posição", ind)
        FimSe
    FimPara

    EscrevaL ("O total de pares foi de", totpar)
fimalgoritmo