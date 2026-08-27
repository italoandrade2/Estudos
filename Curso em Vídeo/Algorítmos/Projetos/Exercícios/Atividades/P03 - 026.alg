// Passo 03 - Condições Compostas (Atividade 26)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 26"

var
    num1, num2: Inteiro
inicio
    Escreva ("Digite o primeiro número: ")
    Leia (num1)
    Escreva ("Digite o segundo número: ")
    Leia (num2)

    Se (num1 > num2) então
        Escreva ("O primeiro valor é o maior")
    senão
        Se (num2 > num1) então
            Escreva ("O segundo número é o maior")
        senão
            Escreva ("Não existe valor maior, os dois são iguais")
        FimSe
    FimSe
fimalgoritmo