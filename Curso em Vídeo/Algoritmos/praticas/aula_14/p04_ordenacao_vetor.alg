// Aula 14 - Prática 4 - Ordenação de Vetor
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Ordenação de Vetor"
var
    vet: vetor[1..10] de Inteiro
    c, j, aux: Inteiro
inicio
    Para c := 1 até 10 faça
        Escreva ("Digite o", c, "º valor: ")
        Leia (vet[c])
    FimPara

    Para c := 1 até 9 faça
        Para j := c+1 até 10 faça
            Se (vet[c] > vet[j]) então
                aux := vet[c]
                vet[c] := vet[j]
                vet[j] := aux
            FimSe
        FimPara
    FimPara

    Para c := 1 até 10 faça
        Escreva ("(", vet[c], ")")
    FimPara
fimalgoritmo