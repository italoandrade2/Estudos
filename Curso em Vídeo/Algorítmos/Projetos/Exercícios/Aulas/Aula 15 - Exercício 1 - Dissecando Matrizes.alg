// Aula 15 - Exercício 1 - Dissecando Matrizes
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Dissecando Matrizes"
var
    val: vetor[1..4, 1..4] de Inteiro
    i, j, op, c2: Inteiro
Procedimento Opcoes()
inicio
    EscrevaL ("MENU DE OPÇÕES")
    EscrevaL ("====================")
    EscrevaL ("[1] Mostrar a Matriz")
    EscrevaL ("[2] Diagonal Principal")
    EscrevaL ("[3] Triângulo Superior")
    EscrevaL ("[4] Triângulo Inferior")
    EscrevaL ("[5] Sair")

    Escreva ("===== OPÇÃO: ")
    Leia (op)
FimProcedimento
inicio
    Para i := 1 até 4 faça
        Para j := 1 até 4 faça
            Escreva ("Digite o valor para a posição [", i, ",", j, "]: ")
            Leia (val[i,j])
        FimPara
    FimPara

    LimpaTela
    Repita
        Opcoes()
        Escolha op
            Caso 1
                LimpaTela
                Para i := 1 até 4 faça
                    Para j := 1 até 4 faça
                        Escreva (val[i,j]:4)
                    FimPara
                    EscrevaL ()
                FimPara
                EscrevaL ()
            Caso 2
                c2 := 4
                LimpaTela
                Para i := 1 até 4 faça
                    Para j := 1 até 4 faça
                        Se (i = j) então
                            Escreva (val[i,j]:c2)
                            c2 := c2 + 4
                        FimSe
                    FimPara
                    EscrevaL ()
                FimPara
                EscrevaL ()
            Caso 3
                LimpaTela
                Para i := 1 até 4 faça
                    Para j := 1 até 4 faça
                        Se (i = j) ou (i = j + 1) ou (i = j + 2) ou (i = j + 3) então
                            Escreva ("    ")
                        senão
                            Escreva (val[i,j]:4)
                        FimSe
                    FimPara
                    EscrevaL ()
                FimPara
                EscrevaL ()
            Caso 4
                LimpaTela
                Para i := 1 até 4 faça
                    Para j := 1 até 4 faça
                        Se (i = j) ou (j = i + 1) ou (j = i + 2) ou (j = i + 3) então
                            Escreva ("    ")
                        senão
                            Escreva (val[i,j]:4)
                        FimSe
                    FimPara
                    EscrevaL ()
                FimPara
                EscrevaL ()
            Caso 5
                LimpaTela
                Escreva("ENCERRANDO...")
        FimEscolha
    Até (op = 5)
fimalgoritmo