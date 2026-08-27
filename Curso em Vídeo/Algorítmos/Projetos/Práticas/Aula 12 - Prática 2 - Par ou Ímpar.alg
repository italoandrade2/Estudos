// Aula 12 - Prática 2 - Par ou Ímpar
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Par ou Ímpar"
var
    numero: Inteiro
Procedimento ParOuImpar(valor: Inteiro)
inicio
    Se (valor % 2 = 0) entao
        EscrevaL ("O número", valor, " é PAR.")
    senao
        EscrevaL ("O número", valor, " é ÍMPAR.")
    FimSe
FimProcedimento
inicio
    Escreva ("Digite um número: ")
    Leia (numero)
    ParOuImpar(numero)
fimalgoritmo