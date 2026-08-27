// Passo 03 - Condições Compostas (Atividade 28)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 28"

var
    lar, alt, area: Inteiro
inicio
    Escreva ("Digite a largura do terreno: ")
    Leia (lar)
    Escreva ("Digite a altura do terreno: ")
    Leia (alt)

    area := lar * alt

    Se (area < 100) então
        Escreva (area, "m² = TERRENO POPULAR")
    senão
        Se (area > 500) então
            Escreva (area, "m² = TERRENO VIP")
        senão
            Escreva (area, "m² = TERRENO MASTER")
        FimSe
    FimSe
fimalgoritmo