// Aula 13 - Prática 1 - Somar dois valores
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Somar dois valores"
var
    V1, V2, S: Inteiro

Função Soma(X, Y: Inteiro): Inteiro
inicio
    Retorne X + Y
FimFunção
inicio
    Escreva ("Digite o primeiro valor: ")
    Leia (V1)
    Escreva ("Digite o segundo valor: ")
    Leia (V2)
    S <- Soma(V1, V2)
    EscrevaL ("A soma entre", V1, " e", V2, " é igual a", S)
fimalgoritmo