// Exercício final
// Italo Andrade Costa
// 26/08/2026 - Versão 1.0

let vendas = [450, 620, 300, 800, 500, 150, 700];
let diabom = 0;
let diafraco = 0;

for (let i = 0; i < vendas.length; i++) {
    if (vendas[i] >= 500) {
        console.log("Dia " + i+1 + ": " + vendas[i] + " (Dia bom)");
        diabom++;
    } else {
        console.log("Dia " + i+1 + ": " + vendas[i] + " (Dia fraco)");
        diafraco++;
    }
}

console.log("Dias bons: " + diabom);
console.log("Dias fracos: " + diafraco);