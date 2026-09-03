// Aula 12 - Prática 3 - Sequência de Fibonacci
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Sequência de Fibonacci"
var
    contador, num1, num2, soma: Inteiro
Procedimento ProximoFibonacci(var A, B: Inteiro)
var
    C: Inteiro
inicio
    C := A + B
    Escreva (C, "..")
    A := B
    B := C
FimProcedimento
inicio
    num1 := 0
    num2 := 1

    Escreva (num1, "..", num2, "..")

    Para contador := 3 até 10 faça
        ProximoFibonacci(num1, num2)
    FimPara
fimalgoritmo