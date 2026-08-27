// Passo 03 - Condições Compostas (Atividade 32)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 32"

var
    num1, num2: Inteiro
inicio
    Escreva ("Adivinhe um numero de 1 a 5: ")
    Leia (num1)
    
    num2 := RandI((5)+1)
    
    Se (num1 > 0) e (num1 < 6) então
        Se (num1 = num2) então
            Escreva ("Parabéns! Você acertou o número.")
        senão
            Escreva ("Que pena! Você errou o número.")
        FimSe
    senão
        Escreva ("Erro. Digite um número de 1 a 5.")
    FimSe
fimalgoritmo