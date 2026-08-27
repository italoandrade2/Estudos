// Aula 14 - Exercício 3 - Reserva de Cinema
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Reserva de Cinema"
var
    cadeira: vetor[1..10] de Caractere
    reserva, c: Inteiro
    resp: Caractere
Procedimento Fileira()
inicio
    Para c := 1 até 10 faça
        Se (cadeira[c] = "") então
            Escreva ("[ B" , c:2, " ]")
        senão
            Escreva ("[ --- ]")
        FimSe
    FimPara
    EscrevaL()
    EscrevaL ("------------------------------------------------------------------------")
FimProcedimento
inicio
    Repita
        LimpaTela
        Fileira()
        Escreva ("Reservar a cadeira: B")
        Leia (reserva)
        Se (cadeira[reserva] = "") então
            EscrevaL ("Cadeira B", reserva:2, " RESERVADA!")
            cadeira[reserva] := "X"
        senão
            EscrevaL ("ERRO. Lugar Ocupado!")
        FimSe
        Escreva ("Quer reservar outro? [S/N] ")
        Leia (resp)
    Até (Maiusc(resp) = "N")
fimalgoritmo