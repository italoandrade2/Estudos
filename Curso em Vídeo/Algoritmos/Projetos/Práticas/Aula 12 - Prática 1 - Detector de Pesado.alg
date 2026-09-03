// Aula 12 - Prática 1 - Detector de Pesado
// Nome: Italo Andrade Costa
// 25/06/2026 - Versão 1.0

algoritmo "Detector de Pesado"
var
    i: Inteiro
    nome, pesado: Caractere
    peso, maior: Real
Procedimento Topo()
inicio
    LimpaTela
    EscrevaL ("------------------------------------")
    EscrevaL (" D E T E C T O R   DE   P E S A D O ")
    EscrevaL ("  Maior Peso até agora:", maior, "Kg  ")
    EscrevaL ("------------------------------------")
FimProcedimento
inicio
    Topo()
    Para i := 1 até 5 faça
        Escreva ("Digite o nome: ")
        Leia (nome)
        Escreva ("Digite o peso de ", nome, ": ")
        Leia (peso)
        Se (peso > maior) então
            maior := peso
            pesado := nome
        FimSe
        Topo()
    FimPara
    Topo()
    EscrevaL ("A pessoa mais pesada foi ", pesado, ", com", maior, " quilos.")
fimalgoritmo
