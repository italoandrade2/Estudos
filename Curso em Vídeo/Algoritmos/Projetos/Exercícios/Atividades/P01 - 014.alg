// Passo 01 - Sequências Básicas (Atividade 14)
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequências Básicas 14"

var
    km, dias, aluguel: Real
inicio
    Escreva ("Digite a quantia de KMs percorridos: ")
    Leia (km)
    Escreva ("Digite a quantia de dias percorridos: ")
    Leia (dias)

    aluguel := (dias*90) + (km * 0.20)

    Escreva ("O valor total do aluguel do carro ficou R$", aluguel:5:2, ".")
fimalgoritmo