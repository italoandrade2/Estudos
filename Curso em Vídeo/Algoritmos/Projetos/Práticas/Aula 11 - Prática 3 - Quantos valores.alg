// Aula 11 - Prática 3 - Quantos valores
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Quantos valores"
var
    contador, numero, total, impar: Inteiro
inicio
    total <- 0
    impar <- 0

    Para contador <- 1 até 6 faça
        Escreva ("Digite um número: ")
        Leia (numero)

        Se (numero >= 0) e (numero <= 10) então
            total <- total + 1
            
            Se (numero % 2 = 1) então
                impar <- impar + numero
            FimSe
        FimSe
    FimPara
    EscrevaL ("Foram", total, " números entre 0 e 10, e a soma dos ímpares desse intervalo é igual a", impar)
fimalgoritmo