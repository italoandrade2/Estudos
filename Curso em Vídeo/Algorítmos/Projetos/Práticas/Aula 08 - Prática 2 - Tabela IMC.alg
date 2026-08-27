// Aula 08 - Prática 2 - Tabela IMC
// Nome: Italo Andrade Costa
// 25/05/2026 - Versão 2.0

algoritmo "Tabela IMC"
var
   massa, altura, IMC: Real
inicio
    Escreva("Digite a sua massa (Kg): ")
    Leia(massa)
    Escreva("Digite a sua altura (m): ")
    Leia(altura)

    IMC <- massa/(altura^2)

    EscrevaL("Dados:")
    EscrevaL(" Massa: ", massa, "kg")
    EscrevaL(" Altura: ", altura:3:2, "m")
    EscrevaL(" IMC: ", IMC:4:2)
    EscrevaL("Resultado:")

    Se(IMC < 17) entao
        EscrevaL(" Muito abaixo do peso.")
    Senao
        Se(IMC >= 17) e (IMC < 18.5) entao
            EscrevaL(" Abaixo do peso.")
        Senao
            Se(IMC >= 18.5) e (IMC < 25) entao
                EscrevaL(" Peso ideal.")
            Senao
                Se(IMC >= 25) e (IMC < 30) entao
                    EscrevaL(" Sobrepeso.")
                Senao
                    Se(IMC < 35) entao
                        EscrevaL(" Obesidade Classe I.")
                    Senao
                        Se(IMC < 40) entao
                            EscrevaL(" Obesidade Classe II.")
                        Senao
                            EscrevaL(" Obesidade Clase III.")
                        FimSe
                    FimSe
                FimSe
            FimSe
        FimSe
    FimSe
fimalgoritmo