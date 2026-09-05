// Aula 10 - Prática 3 - Fatorial
// Nome: Italo Andrade Costa
// 24/06/2026 - Versão 1.0

algoritmo "Fatorial"
var
    numero, contador, fatorial: Inteiro
inicio
    Escreva ("Digite um número: ")
    Leia (numero)
    contador <- numero
    fatorial <- numero

    Escreva (contador)
    Repita
        contador <- contador - 1
        Escreva (" x", contador)
        fatorial <- fatorial * contador
    Até (contador = 1)
    EscrevaL (" =", fatorial)
fimalgoritmo