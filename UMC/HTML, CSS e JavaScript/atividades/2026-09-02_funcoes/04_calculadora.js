const calculadora = {
    n1: 10,
    n2: 5,
    somar() {
        return (this.n1 + this.n2);
    },
    subtrair() {
        return (this.n1 - this.n2);;
    },
    multiplicar() {
        return (this.n1 * this.n2);;
    },
    dividir() {
        return (this.n1 / this.n2);;
    },
};

console.log(calculadora.somar());
console.log(calculadora.subtrair());
console.log(calculadora.multiplicar());
console.log(calculadora.dividir());