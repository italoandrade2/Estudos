// Aula 07 - Prática 1 - Idade
// Nome: Italo Andrade Costa
// 24/05/2026 - Versão 1.0

algoritmo "Idade"
var
    ano, nasc, idade: Inteiro
inicio
    Escreva ("Em que ano estamos? ")
    Leia (ano)
    Escreva ("Em que ano você nasceu? ")
    Leia (nasc)
    idade <- ano - nasc
    Escreva ("Em ", ano, " você terá ", idade, " anos")
    Se (idade >= 21) então
        Escreva (" e já terá atingido a maioridade.")
    FimSe
fimalgoritmo