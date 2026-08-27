// Aula 13 - Prática 3 - Fatorial
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Fatorial"
var
    N, F: Inteiro

Função Fatorial(V: Inteiro): Inteiro
var
    C, R: Inteiro
inicio
    R <- 1
    Para C <- 1 até V faça
        R <- R * C
    FimPara
    Retorne R
FimFunção
inicio
    Escreva ("Digite um número: ")
    Leia (N)
    F <- Fatorial(N)
    EscrevaL ("O valor de", N, "! é igual a", F)
fimalgoritmo