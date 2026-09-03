// Passo 02 - Condições Básicas (Atividade 22)
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Condições Básicas 22"

var
    idade: Inteiro
inicio
    Escreva ("Digite a idade do candidato: ")
    Leia (idade)
    
    Se (idade >= 18) então
        Escreva ("Já se passaram", idade - 18, " ano(s) desde o alistamento do candidato.")
    senão
        Escreva ("Faltam", 18 - idade , " ano(s) para o alistamento do candidato.")
    FimSe
fimalgoritmo