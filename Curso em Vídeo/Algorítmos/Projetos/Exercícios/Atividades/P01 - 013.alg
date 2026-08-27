// Passo 01 - Sequências Básicas (Atividade 13)
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequências Básicas 13"

var
    salario, aumento: Real
inicio
    Escreva ("Digite o valor do salário: R$")
    Leia (salario)

    aumento := salario * (1+0.15)

    Escreva ("O valor do salário com aumento de 15% é igual a R$", aumento:5:2, ".")
fimalgoritmo