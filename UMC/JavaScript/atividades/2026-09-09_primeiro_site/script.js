// Primeiro Site em JavaScript
// Italo Andrade Costa
// 09/09/2026 - Versão 1.0

const campoNome = document.getElementById("nome");
const botaoSaudacao = document.getElementById("btnSaudacao");
const mensagem = document.getElementById("mensagem");

botaoSaudacao.addEventListener("click", function () {
    const nome = campoNome.value;

    if (nome === "") {
        mensagem.textContent = "Digite seu nome!";
    } else {
        mensagem.textContent = "Olá, " + nome + "! Seja bem-vindo(a)!";
    }
});


let contador = 0;

const numero = document.getElementById("contador");

const btnAumentar = document.getElementById("btnAumentar");
const btnDiminuir = document.getElementById("btnDiminuir");
const btnZerar = document.getElementById("btnZerar");

btnAumentar.addEventListener("click", function () {
    contador++;
    numero.textContent = contador;
});

btnDiminuir.addEventListener("click", function () {
    contador--;
    numero.textContent = contador;
});

btnZerar.addEventListener("click", function () {
    contador = 0;
    numero.textContent = contador;
});


const btnCor = document.getElementById("btnCor");
const textoCor = document.getElementById("textoCor");

let cor = false;

btnCor.addEventListener("click", function () {
    if (cor === false) {
        textoCor.style.color = "blue";
        cor = true;
    } else {
        textoCor.style.color = "red";
        cor = false;
    }
});