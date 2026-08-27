// Aula 07 - Exercício 2 - Aluno aprovado ou reprovado?
// Nome: Italo Andrade Costa
// 25/05/2026 - Versão 2.0

algoritmo "Aluno aprovado ou reprovado?"
var
   nota1, nota2, media: Real
inicio
    EscrevaL("-----------------------")
    EscrevaL(" ESCOLA JAVALI CANSADO ")
    EscrevaL("-----------------------")
    Escreva("Primeira Nota: ")
    Leia(nota1)
    Escreva("Segunda Nota: ")
    Leia(nota2)

    EscrevaL("-----------------------")

    media <- (nota1 + nota2)/2
      
    EscrevaL(" MÉDIA:", media)
    Se(media >= 7) entao
        EscrevaL(" ALUNO APROVADO")
    senao
        Se(media >= 5) e (media < 7) entao
            EscrevaL(" ALUNO EM RECUPERAÇÃO")
        senao
            EscrevaL(" ALUNO REPROVADO")
        FimSe
    FimSe
    EscrevaL("-----------------------")
fimalgoritmo