// Aula 09 - Prática 3 - Contar de dez até onde o usuário quiser
// Nome: Italo Andrade Costa
// 27/05/2026 - Versão 1.0

algoritmo "Conte de 0 até onde o usuário quiser"
var
    numero, salto, contador: Inteiro
inicio
    contador <- 0
    Escreva ("Digite um número: ")
    Leia (numero)
    Escreva ("Digite quantos númneros saltar: ")
    Leia (salto)
    
    Enquanto (contador <= numero) faca
        EscrevaL(contador)
        contador <- contador + salto
    FimEnquanto
    EscrevaL("Terminei de contar")
fimalgoritmo