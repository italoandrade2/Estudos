// Aula 06 - Exercício 4 - Imposto
// Nome: Italo Andrade Costa
// 24/05/2026 - Versão 1.0

algoritmo "Imposto"
var
   preço, imposto: Real
inicio
    Escreva("Qual o valor do produto? ")
    Leia(preço)
       
    imposto <- preço * (60/100)
       
    Escreva("O imposto será de U$", imposto)
fimalgoritmo