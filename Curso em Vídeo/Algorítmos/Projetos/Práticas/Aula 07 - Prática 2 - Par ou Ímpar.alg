// Aula 07 - Prática 2 - Par ou Ímpar
// Nome: Italo Andrade Costa
// 24/05/2026 - Versão 1.0

algoritmo "Par ou Ímpar"
var
    n: Inteiro
inicio
    Escreva ("Digite um número qualquer: ")
    Leia (n)
    Se (n % 2 = 0) então
        EscrevaL ("O número ", n, " é PAR")
    senão
        EscrevaL ("O número ", n, " é IMPAR")
    FimSe
fimalgoritmo