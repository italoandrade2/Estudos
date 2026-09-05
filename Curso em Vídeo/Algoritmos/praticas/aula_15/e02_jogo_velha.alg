// Aula 15 - Exercício 2 - Jogo da Velha
// Nome: Italo Andrade Costa
// 08/07/2026 - Versão 1.0

algoritmo "Jogo da Velha"
var
    casa: vetor[1..3, 1..3] de Caractere
    i, j, c, posi: Inteiro
    simb: Caractere
    repetir: Logico
    
Procedimento Velha()
inicio
    EscrevaL ("+---+---+---+")
    Para i := 1 até 3 faça
        Para j := 1 até 3 faça
            Escreva ("|  ", casa[i,j])
        FimPara
        Escreva ("|")
        EscrevaL ()
        EscrevaL ("+---+---+---+")
    FimPara
FimProcedimento

Procedimento Mudar()
inicio
    Se (simb = "X") então
        simb := "O"
    Senão
        simb := "X"
    FimSe
FimProcedimento

Função FimDeJogo(): Logico
var
    terminou: Logico
    vazia: Inteiro
inicio
    terminou := falso

    Para i := 1 até 3 faça
        Se (casa[i, 1] = casa[i, 2]) e (casa[i,2] = casa[i,3]) então
            terminou := verdadeiro
        FimSe
    FimPara

    Para j := 1 até 3 faça
        Se (casa[1,j] = casa[2,j]) e (casa[2,j] = casa[3,j]) então
            terminou := verdadeiro
        FimSe
    FimPara

    Se (casa[1,1] = casa[2,2]) e (casa[2,2] = casa[3,3]) então
        terminou := verdadeiro
    FimSe
    Se (casa[1,3] = casa[2,2]) e (casa[2,2] = casa[3,1]) então
        terminou := verdadeiro
    FimSe

    vazia := 0
    Para i := 1 até 3 faça
        Para j := 1 até 3 faça
            Se (casa[i,j] <> "X") e (casa[i,j] <> "O") então
            vazia := vazia + 1
            FimSe
        FimPara
    FimPara
    Se (vazia = 0) então
        terminou := verdadeiro
    FimSe

    Retorne terminou
FimFunção

Função Jogo(s: Caractere; p: Inteiro): Logico
var mud: Logico
inicio
    mud := falso
    Para i := 1 até 3 faça
        Para j := 1 até 3 faça
            Se (casa[i,j] = NumpCarac(p)) então
                casa[i,j] := s
                mud := verdadeiro
            FimSe
        FimPara
    FimPara
    Retorne mud
FimFunção

inicio
    c := 1
    simb := "X"
    Para i := 1 até 3 faça
        Para j := 1 até 3 faça
            casa[i,j] := NumpCarac(c)
            c := c + 1
        FimPara
    FimPara
    Velha()
    Repita
        Repita
            Escreva ("Vai jogar [", simb:1, "] em qual posição? ")
            Leia (posi)
            repetir := Jogo(simb, posi)
            Se (repetir = falso) então
                EscrevaL ("JOGADA INVÁLIDA!")
            FimSe
        Até (repetir = verdadeiro)
        Mudar()
        LimpaTela
        Velha()
    Até (FimDeJogo() = verdadeiro)
    EscrevaL ("JOGO FINALIZADO!!!")
fimalgoritmo