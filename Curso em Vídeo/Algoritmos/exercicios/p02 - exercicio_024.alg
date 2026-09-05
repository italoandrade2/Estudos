// Passo 02 - Condições Básicas (Atividade 24)
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Condições Básicas 24"

var
    km: Inteiro
    valor: Real
inicio
    Escreva ("Digite a distância em km a ser percorrida: ")
    Leia (km)

    Se (km <= 200) então
        valor := km * 0.50

        Escreva ("O valor da passagem é: R$", valor:5:2)
    senão
        valor := km * 0.45

        Escreva ("O valor da passagem é: R$", valor:5:2)
    FimSe
fimalgoritmo