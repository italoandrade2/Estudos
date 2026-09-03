// Anonymous Function
// Italo Andrade Costa
// 02/09/2026 - Versão 1.0

setTimeout (function () {
    console.log("Executado após 2s");
}, 2000);

const numeros = [1, 2, 3, 4];
const pares = numeros.filter(
    function (n) {
        return n % 2 === 0;
    }
);
console.log(pares);