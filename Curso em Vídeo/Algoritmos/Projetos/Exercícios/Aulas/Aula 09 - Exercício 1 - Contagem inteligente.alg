// Aula 09 - Exercício 1 - Contagem inteligente
// Nome: Italo Andrade Costa
// 28/05/2026 - Versão 1.0

algoritmo "Contagem inteligente"
var
    num1, num2, contador: Inteiro
inicio
    EscrevaL ("CONTAGEM INTELIGENTE")
    EscrevaL ("--------------------")
    Escreva ("Início: ")
    Leia (num1)
    Escreva ("Fim: ")
    Leia (num2)
    EscrevaL ("---------------------")
    EscrevaL ("  C O N T A N D O")
    EscrevaL ("---------------------")

    contador <- num1

    Se (num1 < num2) entao
        Enquanto (contador <= num2) faca
            Escreva (contador, "..")
            contador <- contador + 1
        FimEnquanto
    senao
        Enquanto (num2 <= contador) faca
            Escreva (contador, "..")
            contador <- contador - 1
        FimEnquanto
    FimSe
fimalgoritmo