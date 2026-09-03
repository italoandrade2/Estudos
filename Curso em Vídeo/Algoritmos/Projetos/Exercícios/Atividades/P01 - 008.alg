// Passo 01 - Sequências Básicas (Atividade 08)
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequências Básicas 08"

var
    km, hm, dam, m, dm, cm, mm: Real
inicio
    Escreva ("Digite uma distância em metros: ")
    Leia (m)

    km := m / 1000
    hm := m / 100
    dam := m / 10
    dm := m * 10
    cm := m * 100
    mm := m * 1000

    EscrevaL ("A distância de", m, "m corresponde a:")
    EscrevaL (km:1:5, "Km", "                ", dm:4:1, "dm")
    EscrevaL (hm:1:4, "Hm", "                 ", cm:5:1, "cm" )
    EscrevaL (dam:2:3, "Dam", "                ", mm:6:1, "mm")
fimalgoritmo