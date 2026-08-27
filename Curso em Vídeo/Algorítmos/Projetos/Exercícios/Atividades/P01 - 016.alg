// Passo 01 - Sequências Básicas (Atividade 16)
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequências Básicas 16"

var
    quant, anos, totald, totala, dias: Real
inicio
    Escreva ("Digite a quantia de cigarros fumados por dia: ")
    Leia (quant)
    Escreva ("Digite quantos anos de cigarros fumados:")
    Leia (anos)

    totald := quant*10
    totala := (totald*365)*anos
    dias := totala/1440

    Escreva ("O total de dias de vida perdidos são de ", dias:3:2, ".")
fimalgoritmo