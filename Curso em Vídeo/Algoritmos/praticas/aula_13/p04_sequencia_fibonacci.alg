// Aula 13 - Prática 4 - Sequência de Fibonacci
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequência de Fibonacci"
var
    C, n1, n2, n3: Inteiro

Função Fibonacci(var t1, t2: Inteiro): Inteiro
var
    t3: Inteiro
inicio
    t3 := t1 + t2
    t1 := t2
    t2 := t3
    Retorne t3
FimFunção
inicio
    n1 := 0
    n2 := 1

    Escreva (n1, "..", n2, "..")
    
    Para C := 3 até 5 faça
        n3 := Fibonacci(n1, n2)
        Escreva (n3, "..")
    FimPara
fimalgoritmo