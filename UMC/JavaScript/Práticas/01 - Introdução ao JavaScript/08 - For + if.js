// For + if: um exemplo completo
// Italo Andrade Costa
// 26/08/2026 - Versão 1.0

let notas = [8.5, 4.0, 9.2, 3.5, 6.0];
let aprovados = 0;
let reprovados = 0;

for (let i = 0; i < notas.length; i++) {
    if (notas[i] >= 6) {
        console.log("Nota " + notas[i] + " -> Aprovado");
        aprovados++;
    } else {
        console.log("Nota " + notas[i] + " -> Reprovado");
        reprovados++;
    }
}

console.log("Total de aprovados: " + aprovados);
console.log("Total de reprovados: " + reprovados);