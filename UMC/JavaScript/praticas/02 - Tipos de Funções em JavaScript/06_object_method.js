// Object Method
// Italo Andrade Costa
// 02/09/2026 - Versão 1.0

const pessoa = {
    nome: "Ana",
    saudacao() {
        return `Oi, eu sou ${this.nome}`;
    },
};

console.log(pessoa.saudacao());