// Passo 01 - Sequências Básicas (Atividade 09)
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequências Básicas 09"

var
    reais, dolar: Real
inicio
    Escreva ("Quantos reais você tem? R$")
    Leia (reais)

    dolar := reais / 3.45

    Se (reais < 3.45) então
        dolar := 0
    FimSe

    EscrevaL ("Com R$", reais:4:2, ", você pode comprar $", dolar:4:2, ".")
fimalgoritmo