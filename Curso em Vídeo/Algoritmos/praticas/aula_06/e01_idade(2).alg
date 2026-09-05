// Aula 06 - Exercício 1 - Idade
// Nome: Italo Andrade Costa
// 24/05/2026 - Versão 2.0

algoritmo "Idade"

var
    ano, nasc, idade: Inteiro

inicio
    Escreva("Em que ano estamos? ")
    Leia(ano)
    Escreva("Em que ano você nasceu? ")
    Leia(nasc)
    idade <- ano - nasc
    Escreval("Em ", ano, " você terá ", idade, " anos.")
    Se(idade >= 21) entao
        Escreval("E já terá atingido a maioridade.")
    senao
        Escreval("E você será de menor.")
    FimSe
fimalgoritmo