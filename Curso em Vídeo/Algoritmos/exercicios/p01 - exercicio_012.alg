// Passo 01 - Sequências Básicas (Atividade 12)
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Sequências Básicas 12"

var
    preco, promo: Real
inicio
    Escreva ("Digite o valor do produto: R$")
    Leia (preco)
    
    promo := preco * (1-0.05)

    Escreva ("O valor do produto com desconto de 5% é igual a R$", promo:5:2, ".")
fimalgoritmo