// Function Expression
// Italo Andrade Costa
// 02/09/2026 - Versão 1.0

const somar = function (a, b) {
    return a + b;
};
console.log(somar(3, 4));

// Expressão nomeada (recursão)
const fatorial = function fat(n) {
    if (n <= 1) return 1;
    return n * fat(n - 1);
};
console.log(fatorial(5));