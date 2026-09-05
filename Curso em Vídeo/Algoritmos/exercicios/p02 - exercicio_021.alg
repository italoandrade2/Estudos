// Passo 02 - Condições Básicas (Atividade 21)
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Condições Básicas 21"

var
    ano: Inteiro
inicio
    Escreva ("Digite um ano: ")
    Leia (ano)
    
    Se (ano % 4 = 0) então
        Escreva ("O ano", ano, " é bissexto.")
    senão
        Escreva ("O ano", ano, " não é bissexto.")
    FimSe
fimalgoritmo