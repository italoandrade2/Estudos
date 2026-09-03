// Aula 10 - Prática 4 - Números Primos
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Números Primos"
var
    numero, contador, divisao: Inteiro
    resp: Caractere
inicio
    Repita
        divisao <- 0
        contador <- 1
        Escreva ("Digite um número: ")
        Leia (numero)

        Repita
            Se (numero % contador = 0) entao
                divisao <- divisao + 1
            FimSe

            contador <- contador + 1
        Ate (contador = numero)

        Se (divisao = 2) entao
            EscrevaL ("O número ", numero, " é um número Primo!")
        senao
            EscrevaL ("O número ", numero, " não é um número Primo!")
        FimSe

        EscrevaL ("Deseja continuar (S/N) ")
        Leia (resp)

        LimpaTela
    Até (resp = "N")
    EscrevaL ("Finalizando...")
fimalgoritmo