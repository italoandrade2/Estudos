// Passo 03 - Condições Compostas (Atividade 31)
// Nome: Italo Andrade Costa
// 09/07/2026 - Versão 1.0

algoritmo "Condições Compostas 31"

var
    jog1, jog2: Inteiro
inicio
    EscrevaL ("Pedra = 1")
    EscrevaL ("Papel = 2")
    EscrevaL ("Tesoura = 3")
    Escreva ("Qual será a jogada do jogador 1? ")
    Leia (jog1)
    Escreva ("Qual será a jogada do jogador 2? ")
    Leia (jog2)

    Se (jog1 = 1) então
        Se (jog2 = 2) então
            Escreva ("Vitória do jogador 2!")
        senão
            Se (jog2 = 3) então
                Escreva ("Vitória do jogador 1!")
            senão
                Escreva ("Empate!")
            FimSe
        FimSe
    senão
        Se (jog1 = 2) então
            Se (jog2 = 1) então
                Escreva ("Vitória do jogador 1!")
            senão
                Se (jog2 = 3) então
                    Escreva ("Vitória do jogador 2!")
                senão
                    Escreva ("Empate!")
                FimSe
            FimSe
        senão
            Se (jog2 = 1) então
                Escreva ("Vitória do jogador 2!")
            senão
                Se (jog2 = 2) então
                    Escreva ("Vitória do jogador 1!")
                senão
                    Escreva ("Empate!")
                FimSe
            FimSe    
        FimSe
    FimSe
fimalgoritmo