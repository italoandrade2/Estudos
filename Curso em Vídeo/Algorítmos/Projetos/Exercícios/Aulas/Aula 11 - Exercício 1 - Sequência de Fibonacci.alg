// Aula 11 - Exercício 1 - Sequência de Fibonacci
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Sequência de Fibonacci"
var
    contador, n1, n2, soma: Inteiro
inicio
    n1 := 0
    n2 := 1
    soma := 0
    Escreva (n1, n2)

    Para contador := 1 até 13 faça
        soma := n1 + n2
        Escreva (soma)

        n1 := n2
        n2 := soma
    FimPara
fimalgoritmo
