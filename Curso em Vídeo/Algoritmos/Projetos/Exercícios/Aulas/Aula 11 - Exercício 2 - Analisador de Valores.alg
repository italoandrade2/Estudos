// Aula 11 - Exercício 2 - Analisador de Valores
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Analisador de Valores"
var
    numero, contador, soma, div5, nulos, pares: Inteiro
    media: Real
inicio
    soma := 0
    div5 := 0
    nulos := 0
    pares := 0

    Para contador := 1 até 5 faça
        Escreva ("Digite o", contador, "º valor: ")
        Leia (numero)
        soma := soma + numero

        Se (numero % 5 = 0) então
            div5 := div5 + 1
        FimSe

        Se (numero = 0) então
            nulos := nulos + 1
        FimSe

        Se (numero % 2 = 0) então
            pares := pares + numero
        FimSe
    FimPara

    media := soma / 5

    EscrevaL ("A soma entre os valores é:", soma)
    EscrevaL ("A média entre os valores é", media)
    EscrevaL ("Valores divisíveis por cinco:", div5)
    EscrevaL ("Valores nulos:", nulos)
    EscrevaL ("A soma dos valores pares é", pares)
fimalgoritmo
