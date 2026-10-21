// Análise de Vendas da Semana
// Italo Andrade Costa
// 26/08/2026 - Versão 1.0

let vendas = [450, 620, 300, 800, 500, 150, 700];
let total = 0;
let diasBons = 0;
let diasFracos = 0;

for (let i = 0; i < vendas.length; i++) {
    total += vendas[i];
    if (vendas[i] >= 500) {
        console.log("Dia bom");
        diasBons++;
    } else {
        console.log("Dia fraco");
        diasFracos++;
    }
}

console.log("Total da semana: " + total);
console.log("Dias bons: " + diasBons);
console.log("Dias fracos: " + diasFracos);