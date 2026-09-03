// Aula 13 - Prática 2 - Par ou Ímpar
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Par ou Ímpar"
var
    N: Inteiro
    R: Caractere
Função ParOuImpar(V: Inteiro): Caractere
inicio
    Se (V % 2 = 0) então
        Retorne "par."
    senão
        Retorne "ímpar."
    FimSe
FimFunção
inicio
    Escreva ("Digite um número: ")
    Leia (N)
    R <- ParOuImpar(N)
    EscrevaL ("O número", N, " é um valor ", R)
fimalgoritmo