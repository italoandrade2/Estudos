// Aula 08 - Prática 1 - Média Aluno
// Nome: Italo Andrade Costa
// 25/05/2026 - Versão 2.0

algoritmo "Média Aluno"
var
   n1, n2, m: Real
inicio
    Escreva("Primeira Nota: ")
    Leia(n1)
    Escreva("Segunda Nota: ")
    Leia(n2)

    m <- (n1 + n2) / 2

    EscrevaL("A média do aluno foi ", m:4:2)
    
    Se (m >= 7) entao
        EscrevaL("Aluno APROVADO")
    Senao
        Se(m >= 5) e (m < 7) entao
            EscrevaL("Aluno em RECUPERAÇÃO")
        Senao
            EscrevaL("Aluno REPROVADO")
        FimSe
    FimSe
fimalgoritmo