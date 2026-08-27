// Passo 03 - Condições Compostas (Atividade 30)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 30"

var
    lado1, lado2, lado3: Inteiro
    area: Real
inicio
    Escreva ("Digite o tamanho da primeira reta: ")
    Leia (lado1)
    Escreva ("Digite o tamanho da segunda reta: ")
    Leia (lado2)
    Escreva ("Digite o tamanho da terceira reta: ")
    Leia (lado3)

    Se (lado1 < (lado2 + lado3)) e (lado2 < (lado1 + lado3)) e (lado3 < (lado1 + lado2)) então
        Se (lado1 = lado2) e (lado2 = lado3) então
            Escreva ("Um triângulo EQUILÁTERO será formado com essas medidas.")
        senão
            Se (lado1 = lado2) ou (lado2 = lado3) ou (lado1 = lado3) então
                Escreva ("Um triângulo ISÓCELES será formado com essas medidas.")
            senão
                Escreva ("Um triângulo ESCALENO será formado com essas medidas.")
            FimSe    
        FimSe
    senão
        Escreva ("Não é possível formar um triângulo com essas medidas.")
    FimSe
fimalgoritmo