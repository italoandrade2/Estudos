// A instrução Switch
// Italo Andrade Costa
// 26/08/2026 - Versão 1.0

let diaSemana = 3;
let nomeDia;

switch (diaSemana) {
    case 1:
        nomeDia = "Domingo";
        break;
    case 2:
        nomeDia = "Segunda-Feira";
        break;
    case 3:
        nomeDia = "Terça-Feira";
        break;
    default:
        nomeDia = "Dia inválido";
}

console.log(nomeDia);