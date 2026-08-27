// Aula 07 - Prática 3 - Cálculo do IMC
// Nome: Italo Andrade Costa
// 24/05/2026 - Versão 1.0

algoritmo "Cálculo do IMC"
var
    m, a, imc: Real
inicio
    Escreva ("Massa (Kg): ")
    Leia (m)
    Escreva ("Altura (m): ")
    Leia (a)
    imc <- m / (a ^ 2)
    EscrevaL ("IMC: ", imc:5:2)
    Se (imc >= 18.5) e (imc < 25) então
        EscrevaL ("Parabéns! Você está no seu peso ideal")
    senão
        EscrevaL ("Você não está na faixa de peso ideal")
    FimSe
fimalgoritmo