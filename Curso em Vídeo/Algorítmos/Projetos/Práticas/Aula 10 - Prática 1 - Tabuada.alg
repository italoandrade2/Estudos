// Aula 10 - Prática 1 - Tabuada
// Nome: Italo Andrade Costa
// 28/05/2026 - Versão 1.0

algoritmo "Tabuada"
var
    numero, contador, resultado: Inteiro
inicio
    contador <- 1
    Escreva ("Digite um número: ")
    Leia (numero)

    Repita
        resultado <- numero * contador
        EscrevaL(numero, " x", contador, " =", resultado)
        contador <- contador + 1
    Até (contador > 10)
fimalgoritmo