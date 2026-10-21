// Generator Function
// Italo Andrade Costa
// 02/09/2026 - Versão 1.0

function* contador() {
    yield 1;
    yield 2;
    yield 3;
}

const gerador = contador();
console.log(gerador.next().value);
console.log(gerador.next().value);
console.log(gerador.next().value);