// Passo 02 - Condições Básicas (Atividade 25)
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Condições Básicas 25"

var
    lado1, lado2, lado3: Inteiro
inicio
    Escreva ("Digite o tamanho da primeira reta: ")
    Leia (lado1)
    Escreva ("Digite o tamanho da segunda reta: ")
    Leia (lado2)
    Escreva ("Digite o tamanho da terceira reta: ")
    Leia (lado3)

    Se (lado1 < (lado2 + lado3)) e (lado2 < (lado1 + lado3)) e (lado3 < (lado1 + lado2)) então
        Escreva ("É possível formar um triângulo com essas medidas.")
    senão
        Escreva ("Não é possível formar um triângulo com essas medidas.")
    FimSe
fimalgoritmo