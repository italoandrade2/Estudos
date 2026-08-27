// Aula 10 - Exercício 2 - Seletor de Pessoas
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Seletor de Pessoas"
var
    cabelo, idade, conthom, contmul: Inteiro
    genero, resp: Caractere
inicio
    conthom <- 0
    contmul <- 0

    Repita
        EscrevaL ("==========================")
        EscrevaL ("    SELETOR DE PESSOAS    ")
        EscrevaL ("==========================")

        Escreva ("Qual o Sexo? [M/F] ")
        Leia (genero)

        Escreva ("Qual a idade? ")
        Leia (idade)

        EscrevaL ("Qual a cor do Cabelo?")
        EscrevaL ("---------------------")
        EscrevaL ("[1] Preto")
        EscrevaL ("[2] Castanho")
        EscrevaL ("[3] Loiro")
        EscrevaL ("[4] Ruivo")
        Leia (cabelo)

        Se (genero = "M") e (idade > 18) e (cabelo = 2) entao
                    conthom <- conthom + 1
        FimSe

        Se (genero = "F") e (idade >= 25) e (idade <= 30) e (cabelo = 3) entao
                    contmul <- contmul + 1
        FimSe

        Escreva ("Quer continuar? [S/N] " )
        Leia (resp)
        LimpaTela
    Até (resp = "N")

    EscrevaL ("------------------------------------")
    EscrevaL (" RESULTADO FINAL")
    EscrevaL ("------------------------------------")
    EscrevaL ("Total de homens com mais de 18 e cabelos castanhos:", conthom)
    EscrevaL ("Total de mulheres entre 25 e 30 e cabelos loiros:", contmul)
fimalgoritmo