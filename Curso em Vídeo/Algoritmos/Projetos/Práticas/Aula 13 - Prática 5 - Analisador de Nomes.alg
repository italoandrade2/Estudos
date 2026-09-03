// Aula 13 - Prática 5 - Analisador de Nomes
// Nome: Italo Andrade Costa
// 06/07/2026 - Versão 1.0

algoritmo "Analisador de Nomes"
var
    C: Inteiro
    nome: Caractere
inicio
    Escreva ("Digite seu nome: ")
    Leia (nome)
    EscrevaL ("Total de letras do seu nome:", Compr(nome))
    EscrevaL ("Seu nome em maiúsculas é: ", Maiusc(nome))
    EscrevaL ("Seu nome em minúsculas é: ", Minusc(nome))
    EscrevaL ("A primeira letra do seu nome é: ", Copia(nome, 1, 1))
    EscrevaL ("A última letra do seu nome é: ", Copia(Maiusc(nome), Compr(nome), 1))
    EscrevaL ("Seu nome tem a letra A na posição", Pos("A", Maiusc(nome)))
    EscrevaL ("O código da letra A é", Asc("A"))
    EscrevaL ("A letra de código 65 é ", Carac(65))

    Para C := Compr(nome) até 1 passo -1 faça
        Escreva (Copia(Maiusc(nome), C, 1))
    FimPara
fimalgoritmo