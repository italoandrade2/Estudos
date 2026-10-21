// Constructor Function
// Italo Andrade Costa
// 02/09/2026 - Versão 1.0

function Carro(marca, modelo) {
    this.marca = marca;
    this.modelo = modelo;
}

const meuCarro = new Carro("Toyota", "Corolla");
console.log(meuCarro.marca);