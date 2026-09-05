// Passo 02 - Condições Básicas (Atividade 17)
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Condições Básicas 17"

var
    vel, max: Inteiro
inicio
    Escreva ("Qual a velocidade do veículo? ")
    Leia (vel)

    Se (vel > 80) então
        max := vel - 80
        Escreva ("Você ultrapassou o limite de velocidade. Você será multado em R$", max:4:2, ".")
    senão
        Escreva ("Você está dentro do limite de velocidade.")
    FimSe
fimalgoritmo