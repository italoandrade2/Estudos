// Aula 10 - Prática 2 - Negativos
// Nome: Italo Andrade Costa
// 28/05/2026 - Versão 1.0

algoritmo "Negativos"
var
    numero, contador, negativo: Inteiro
inicio
    contador <- 1
    negativo <- 0

    Repita
        Escreva ("Digite um número: ")
        Leia (numero)
        Se (numero < 0) entao
            negativo <- negativo + 1
        FimSe
        contador <- contador + 1
    Até (contador > 5)
    EscrevaL ("O total de números negativos é de", negativo)
fimalgoritmo