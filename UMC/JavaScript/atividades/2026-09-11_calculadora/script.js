// Primeiro Site JavaScript (com calculadora)
// Nome: Italo Andrade Costa
// 11/09/2026

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


let calculadora = 0;

let primeiroNumero;
let operacao;
let segundoNumero;

let etapa = "primeiroNumero"

const calculo = document.getElementById("calculo");
const etapaAtual = document.getElementById("etapaAtual");
const btnNum1 = document.getElementById("btnNum1");
const btnNum2 = document.getElementById("btnNum2");
const btnNum3 = document.getElementById("btnNum3");
const btnNum4 = document.getElementById("btnNum4");
const btnNum5 = document.getElementById("btnNum5");
const btnNum6 = document.getElementById("btnNum6");
const btnNum7 = document.getElementById("btnNum7");
const btnNum8 = document.getElementById("btnNum8");
const btnNum9 = document.getElementById("btnNum9");
const btnNum0 = document.getElementById("btnNum0");

const btnSomar = document.getElementById("btnSomar");
const btnSubtrair = document.getElementById("btnSubtrair");
const btnIgual = document.getElementById("btnIgual");

btnNum1.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 1;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 1;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 1;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum2.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 2;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 2;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 2;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum3.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 3;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 3;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 3;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum4.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 4;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 4;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 4;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum5.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 5;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 5;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 5;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum6.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 6;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 6;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 6;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum7.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 7;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 7;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 7;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum8.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 8;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 8;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 8;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum9.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 9;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 9;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 9;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnNum0.addEventListener("click", function () {
    if (etapa === "primeiroNumero") {
        primeiroNumero = 0;
        etapa = "operacao";
        etapaAtual.textContent = "Digite a operação:"
        calculadora = 0;
        calculo.textContent = calculadora;
    } else if (etapa === "segundoNumero") {
        segundoNumero = 0;
        etapa = "resultado";
        calculadora = primeiroNumero + " " + operacao + " " + segundoNumero;
        calculo.textContent = calculadora;
    }
});

btnSomar.addEventListener("click", function () {
    if (etapa === "operacao") {
        operacao = "+";
        etapa = "segundoNumero";
        etapaAtual.textContent = "Digite o segundo número:"
        calculadora = primeiroNumero + " +";
        calculo.textContent = calculadora;
    }
});

btnSubtrair.addEventListener("click", function () {
    if (etapa === "operacao") {
        operacao = "-";
        etapa = "segundoNumero"
        etapaAtual.textContent = "Digite o segundo número:"
        calculadora = primeiroNumero + " -";
        calculo.textContent = calculadora;
    };
});

btnIgual.addEventListener("click", function () {
    if (etapa === "resultado") {
        etapaAtual.textContent = "Resultado:"

        if (operacao === "+") {
            soma = primeiroNumero + segundoNumero;
            calculadora = primeiroNumero + " " + operacao + " " + segundoNumero + " = " + soma;
            calculo.textContent = calculadora;
            etapa = "finalizado"
        } else {
            subtracao = primeiroNumero - segundoNumero;
            calculadora = primeiroNumero + " " + operacao + " " + segundoNumero + " = " + subtracao;
            calculo.textContent = calculadora;
            etapa = "finalizado"
        }
    }
    numero.textContent = contador;
});

btnReiniciar.addEventListener("click", function () {
    calculadora = 0;
    calculo.textContent = calculadora;
    etapa = "primeiroNumero"
    etapaAtual.textContent = "Digite o primeiro número:"
})