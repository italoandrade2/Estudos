// Aula 10 - Exercício 1 - Super Contador
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Super Contador"
var
    numero, contador: Inteiro
    resp: Caractere
inicio
    Repita
        EscrevaL ("")
        EscrevaL ("=================")
        EscrevaL ("|    M E N U    |")
        EscrevaL ("=================")
        EscrevaL ("| [1] De 1 a 10 |")
        EscrevaL ("| [2] De 10 a 1 |")
        EscrevaL ("| [3] Sair      |")
        EscrevaL ("=================")
        Leia (numero)

        Escolha numero
            Caso 1
                contador <- 1

                Repita
                    Escreva (contador, "..")
                    contador <- contador + 1
                Até (contador > 10)
            Caso 2
                contador <- 10

                Repita
                    Escreva (contador, "..")
                    contador <- contador - 1
                Até (contador < 1)
            Caso 3
                EscrevaL ("SAINDO...")
            OutroCaso
                EscrevaL ("INVÁLIDO!")     
        FimEscolha
    Até (numero = 3)       
fimalgoritmo