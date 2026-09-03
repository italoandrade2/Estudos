// Aula 09 - Prática 4 - Soma 10 números
// Nome: Italo Andrade Costa
// 28/05/2026 - Versão 1.0

algoritmo "Soma 10 números"
var
    numero, numeros, soma, maior, menor: Inteiro
inicio
    numeros <- 1
    soma <- 0
    
    Enquanto (numeros <= 10) faca
        Escreva("Digite o ", numeros, "º numero: ")
        Leia(numero)
        Se (numero > maior) entao
            maior <- numero
        FimSe
        Se (numeros = 1) entao
            menor <- numero
        senao
             Se (numero < menor) entao
                menor <- numero
             FimSe
        FimSe
        soma <- soma + numero
        numeros <- numeros + 1
    FimEnquanto
    EscrevaL("A soma desses 10 números é igual a", soma)
    EscrevaL("O maior número é o", maior, ", e o menor número é o", menor)
fimalgoritmo