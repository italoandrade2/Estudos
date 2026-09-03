// Aula 07 - Exercício 2 - Aluno aprovado ou reprovado?
// Nome: Italo Andrade Costa
// 24/05/2026 - Versão 1.0

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
        EscrevaL(" ALUNO REPROVADO")
    FimSe
    EscrevaL("-----------------------")
fimalgoritmo