// Aula 06 - Exercício 5 - Empréstimo
// Nome: Italo Andrade Costa
// 24/05/2026 - Versão 1.0

algoritmo "Imposto"
var
   valor, valor_juros, valor_parcela: Real
   parcelas: Inteiro
inicio
    Escreva("Qual o valor do empréstimo? ")
    Leia(valor)
    valor_juros <- valor * 1.20
    Escreva("Em quantas parcelas irei pagar? ")
    Leia(parcelas)    
    valor_parcela <- valor_juros / parcelas
       
    Escreva("Eu irei pagar o empréstimo em ", parcelas, " parcelas de R$", valor_parcela)
fimalgoritmo