// Aula 06 - Exercício 1 - Idade
// Nome: Italo Andrade Costa
// 21/05/2026 - Versão 1.0

algoritmo "Idade"

var
    ano_atual, ano_nasc, idade: Inteiro

inicio
    Escreva("Em que ano nós estamos? ")
    Leia(ano_atual)
    Escreva("Em que ano eu nasci? ")
    Leia(ano_nasc)
       
    idade <- ano_atual - ano_nasc
       
    Escreva("Eu tenho ", idade, " anos!")
fimalgoritmo