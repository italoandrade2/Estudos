// Passo 03 - Condições Compostas (Atividade 33)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 33"

var
    val, sal, prest, lim: Real
    anos: Inteiro
inicio
    Escreva ("Digite o valor da casa: R$")
    Leia (val)
    Escreva ("Digite o seu salário: R$")
    Leia (sal)
    Escreva ("Por quantos anos deseja pagar o imóvel? ")
    Leia (anos)

    prest := val / (anos*12)
    lim := sal * 0.3

    Se (prest <= lim) então
        Escreva ("Parabéns! Seu empréstimo foi aprovado.")
    senão
        Escreva ("Que pena! Seu empréstimo foi negado.")
    FimSe
fimalgoritmo