// Aula 09 - Prática 5 - Converter moedas
// Nome: Italo Andrade Costa
// 28/05/2026 - Versão 1.0

algoritmo "Converter moedas"
var
   reais, dolar: Real
   conversor, quantia: Inteiro
inicio
    conversor <- 1

    Escreva ("Quantas vezes você quer converter? ")
    Leia(quantia)

    Enquanto (conversor <= quantia) faca
        Escreva("Quantos reais eu tenho? ")
        Leia(reais)

        dolar <- reais / 5.02

        conversor <- conversor + 1
        EscrevaL("Eu poderei ter U$", dolar:5:2)
    FimEnquanto
fimalgoritmo