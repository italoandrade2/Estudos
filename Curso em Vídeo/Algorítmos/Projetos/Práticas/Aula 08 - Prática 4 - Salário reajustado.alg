// Aula 08 - Prática 5 - Reajuste de Salário
// Nome: Italo Andrade Costa
// 25/05/2026 - Versão 1.0

algoritmo "Reajuste de Salário"
var
   nome: Caractere
   sal1, sal2: Real
   dep: Inteiro
inicio
      Escreva ("Qual o nome do funcionário? ")
      Leia (nome)
      Escreva ("Qual o salário de ", nome, "? R$")
      Leia (sal1)
      Escreva ("Qual é a quantidade de dependentes? ")
      Leia (dep)
      Escolha dep
              Caso 0
                   sal2 <- sal1 + (sal1*5/100)
              Caso 1, 2, 3
                   sal2 <- sal1 + (sal1*10/100)
              Caso 4, 5, 6
                   sal2 <- sal1 + (sal1*15/100)
              OutroCaso
                   sal2 <- sal1 + (sal1*18/100)
      FimEscolha
      EscrevaL ("O novo salário de ", nome, " será de R$", sal2:5:2)
fimalgoritmo