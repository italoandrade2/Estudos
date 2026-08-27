// Passo 03 - Condições Compostas (Atividade 27)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 27"

var
    n1, n2, media: Real
inicio
    Escreva ("Digite a primeira nota: ")
    Leia (n1)
    Escreva ("Digite a segunda nota: ")
    Leia (n2)

    media := (n1 + n2) / 2

    Se (media < 5) então
        Escreva ("Média:", media, " = REPROVADO")
    senão
        Se (media >= 7) então
            Escreva ("Média:", media, " = APROVADO")
        senão
            Escreva ("Média:", media, " = RECUPERAÇÃO")
        FimSe
    FimSe
fimalgoritmo