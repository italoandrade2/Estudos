// Passo 01 - Sequências Básicas (Atividade 10)
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequências Básicas 10"

var
    larg, alt, area, tinta: Real
inicio
    Escreva ("Digite a largura: ")
    Leia (larg)
    Escreva ("Digite a altura: ")
    Leia (alt)

    area := larg*alt

    tinta := area / 2

    Escreva ("Para pintar uma área de ", area:2:1, "m², você precisará de ", tinta:2:1, " litros de tinta.")
fimalgoritmo