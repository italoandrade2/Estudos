// Passo 02 - Condições Básicas (Atividade 23)
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Condições Básicas 23"

var
    nome, gen: Caractere
    valor, total: Real
inicio
    Escreva ("Digite seu nome: ")
    Leia (nome)
    Escreva ("Digite seu gênero (M/F): ")
    Leia (gen)
    Escreva ("Digite o valor da compra: R$")
    Leia (valor)

    Se (Maiusc(gen) = "M") então
        total := valor * (1 - 0.05)

        EscrevaL ("Cliente: ", nome)
        EscrevaL ("Valor da compra: R$", valor:6:2)
        EscrevaL ("Desconto aplicado: 5%")
        EscrevaL ("Valor final: R$", total:6:2)
    senão
        Se (Maiusc(gen) = "F") então
            total := valor * (1 - 0.13)

            EscrevaL ("Cliente: ", nome)
            EscrevaL ("Valor da compra: R$", valor:6:2)
            EscrevaL ("Desconto aplicado: 13%")
            EscrevaL ("Valor final: R$", total:6:2)
        senão
            EscrevaL ("Erro. Gênero incorreto.")
        FimSe
    FimSe
fimalgoritmo