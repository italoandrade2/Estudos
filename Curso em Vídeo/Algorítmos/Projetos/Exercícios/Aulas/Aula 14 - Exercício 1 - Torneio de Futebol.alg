// Aula 14 - Exercício 1 - Torneio de Futebol
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Torneio de Futebol"
var
    time: vetor[1..3] de Caractere
    i, j: Inteiro
inicio
    EscrevaL ("---------------------")
    EscrevaL ("CAMPEONATO DE FUTEBOL")
    EscrevaL ("---------------------")
    Para i := 1 até 3 faça
        Escreva ("Nome do", i, "º time: ")
        Leia (time[i])
    FimPara

    LimpaTela
    EscrevaL ("--------------------")
    EscrevaL (" TABELA DE PARTIDAS")
    EscrevaL ("--------------------")    
    Para i := 1 até 3 faça
        Para j := 1 até 3 faça
            Se (i <> j) então
                EscrevaL (time[i]:13, "[ ] x [ ] ", time[j])
            FimSe
        FimPara
    FimPara
fimalgoritmo