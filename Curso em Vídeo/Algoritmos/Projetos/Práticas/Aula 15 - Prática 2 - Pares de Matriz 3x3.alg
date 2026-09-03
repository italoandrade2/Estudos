// Aula 15 - Prática 2 - Pares de Matriz 3x3
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Pares de Matriz 3x3"
var
    val: vetor[1..3, 1..3] de Inteiro
    l, c, total: Inteiro
inicio
    Para l := 1 até 3 faça
        Para c := 1 até 3 faça
            Escreva ("Digite o valor da posição [", l, ",", c, "]: ")
            Leia (val[l, c])
        FimPara
    FimPara

    EscrevaL ()
    EscrevaL ("MATRIZ:")
    EscrevaL ("----------------")

    total := 0
    Para l := 1 até 3 faça
        Para c := 1 até 3 faça
            Se (val[l, c] % 2 = 0) então
                Escreva ("{", val[l,c]:2, "}")
                total := total + 1
            senão
                Escreva (val[l, c]:4)
            FimSe
        FimPara
        EscrevaL ()
    FimPara
    
    EscrevaL ("Ao todo foram digitados", total, " valores PARES.")
fimalgoritmo