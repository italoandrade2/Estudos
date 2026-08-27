// Aula 08 - Exercício 2 - Uma partida de futebol
// Nome: Italo Andrade Costa
// 26/05/2026 - Versão 1.0

algoritmo "Aproveitamento de um aluno"
var
    bangu, madureira, diferenca: Inteiro
    status: Caractere
inicio
    EscrevaL ("   BANGU X MADUREIRA  ")
    EscrevaL ("-----------------------")
    Escreva ("Quantos gols do BANGU? ")
    Leia (bangu)
    Escreva ("Quantos gols do MADUREIRA? ")
    Leia (madureira)
    EscrevaL ("-----------------------")

    Se (bangu > madureira) entao
        diferenca <- bangu - madureira
    senao
        diferenca <- madureira - bangu
    FimSe
    EscrevaL(" DIFERENÇA:", diferenca)

    Escolha diferenca
        Caso 0
            EscrevaL (" STATUS: EMPATE")
        Caso 1, 2, 3
            EscrevaL (" STATUS: PARTIDA NORMAL")
        Caso 4, 5, 6, 7
            EscrevaL (" STATUS: GOLEADA")
    FimEscolha
    EscrevaL("-----------------------")
fimalgoritmo