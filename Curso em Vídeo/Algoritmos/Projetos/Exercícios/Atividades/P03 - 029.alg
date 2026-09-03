// Passo 03 - Condições Compostas (Atividade 29)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 29"

var
    nome: Caractere
    anos: Inteiro
    sal1, sal2: Real
inicio
    Escreva ("Digite o nome do funcionário: ")
    Leia (nome)
    Escreva ("Digite o salário do funcionário: ")
    Leia (sal1)
    Escreva ("Digite o tempo em anos do funcionário: ")
    Leia (anos)

    Se (anos <= 3) então
        sal2 := sal1 * 1.03
        Escreva (anos, " anos de empresa (3%): R$", sal2:4:2)
    senão
        Se (anos >= 10) então
            sal2 := sal1 * 1.20
            Escreva (anos, " anos de empresa (20%): R$", sal2:4:2)
        senão
            sal2 := sal1 * 1.125
            Escreva (anos, " anos de empresa (12.5%): R$", sal2:4:2)
        FimSe
    FimSe
fimalgoritmo