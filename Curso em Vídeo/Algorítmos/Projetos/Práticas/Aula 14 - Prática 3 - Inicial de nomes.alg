// Aula 14 - Prática 3 - Inicial de nomes
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Inicial de nomes"
var
    nome: Caractere
    soC: vetor[1..10] de Caractere
    c, total: Inteiro
inicio
    total := 0

    Para c := 1 até 10 faça
        Escreva ("Digite o", c, "º nome: ")
        Leia (nome)

        Se (Copia(Maiusc(nome), 1, 1) = "C") então
            total := total + 1
            soC[total] := nome
        FimSe
    FimPara

    LimpaTela
    EscrevaL ("LISTAGEM FINAL")
    Para c := 1 até total faça
        EscrevaL (soC[c])
    FimPara
fimalgoritmo