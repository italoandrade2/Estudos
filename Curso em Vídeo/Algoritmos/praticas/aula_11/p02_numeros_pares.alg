// Aula 11 - Prática 2 - Números Pares
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Números Pares"
var
    contador, numero: Inteiro
inicio
    Escreva ("Digite um número: ")
    Leia (numero)

    Se (numero % 2 = 1) entao
        numero <- numero - 1
    FimSe

    Para contador <- numero até 0 passo -2 faça
        Escreva (contador, "..")
    FimPara
fimalgoritmo