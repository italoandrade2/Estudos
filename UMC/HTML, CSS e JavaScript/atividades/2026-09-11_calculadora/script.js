// Primeiro Site JavaScript (com calculadora)
// Nome: Italo Andrade Costa
// 11/09/2026

// Saudação

const campoNome = document.getElementById("nome");
const botaoSaudacao = document.getElementById("btnSaudacao");
const botaoResetar = document.getElementById("btnResetar");
const mensagem = document.getElementById("mensagem");

botaoSaudacao.addEventListener("click", function () {
    const nome = campoNome.value;

    if (nome === "") {
        mensagem.textContent = "Digite seu nome!";
    } else {
        mensagem.textContent = "Olá, " + nome + "! Seja bem-vindo(a)!";
    }
});

botaoResetar.addEventListener("click", function () {
    const nome = campoNome.value;

    if (nome != "") {
        mensagem.textContent = "Digite seu nome e clique no botão."
    }
})

// Contador

let contador = 0;

const numero = document.getElementById("contador");

const btnAumentar = document.getElementById("btnAumentar");
const btnDiminuir = document.getElementById("btnDiminuir");
const btnZerar = document.getElementById("btnZerar");

function atualizarBotoes() {
    btnAumentar.disabled = contador >= 10;
    btnDiminuir.disabled = contador <= 0;
}

btnAumentar.addEventListener("click", function () {
    contador++;
    numero.textContent = contador;
    atualizarBotoes();
});

btnDiminuir.addEventListener("click", function () {
    contador--;
    numero.textContent = contador;
    atualizarBotoes();
});

btnZerar.addEventListener("click", function () {
    contador = 0;
    numero.textContent = contador;
    atualizarBotoes();
});

// Trocar cor

const btnCor = document.getElementById("btnCor");
const textoCor = document.getElementById("textoCor");

const cores = ["black", "red", "lime", "blue", "yellow", "cyan", "magenta", "silver"];
index = 0;
let cor = "black";

btnCor.addEventListener("click", function () {
    if (cor === "silver") {
        index = 0;
        cor = cores[index];
        textoCor.style.color = cor;
    } else {
        index++;
        cor = cores[index];
        textoCor.style.color = cor;
    }
});

// Calculadora

const btnSomar = document.getElementById("btnSomar");
const btnSubtrair = document.getElementById("btnSubtrair");
const btnMultiplicar = document.getElementById("btnMultiplicar");
const btnDividir = document.getElementById("btnDividir");
const btnLimpar = document.getElementById("btnLimpar");

const campoNum1 = document.getElementById("number1");
const campoNum2 = document.getElementById("number2");
const resultado = document.getElementById("resultado");

function pegarNumeros() {
    const n1 = Number(campoNum1.value);
    const n2 = Number(campoNum2.value);
    if (campoNum1.value === "" || campoNum2.value === "") {
        resultado.textContent = "Preencha os dois campos!";
        return null;
    }

    return { n1, n2 };
}

btnSomar.addEventListener("click", function () {
    const numeros = pegarNumeros();
    if (numeros === null) return;
    
    resultado.textContent = "Resultado: " + (numeros.n1 + numeros.n2);
});

document.addEventListener("keydown", function () {
    if (event.key === "Enter") {
        const numeros = pegarNumeros();
        if (numeros === null) return;
    
        resultado.textContent = "Resultado: " + (numeros.n1 + numeros.n2);
    }
})

btnSubtrair.addEventListener("click", function () {
    const numeros = pegarNumeros();
    if (numeros === null) return;
    
    resultado.textContent = "Resultado: " + (numeros.n1 - numeros.n2);
});

btnMultiplicar.addEventListener("click", function () {
    const numeros = pegarNumeros();
    if (numeros === null) return;
    
    resultado.textContent = "Resultado: " + (numeros.n1 * numeros.n2);
});

btnDividir.addEventListener("click", function () {
    const numeros = pegarNumeros();
    if (numeros === null) return;
    
    if (numeros.n2 === 0) {
        resultado.textContent = "Resultado: Erro! Impossível dividir por zero."
    } else {
        resultado.textContent = "Resultado: " + (numeros.n1 / numeros.n2);
    };
});

btnLimpar.addEventListener("click", function () {
    campoNum1.value = "";
    campoNum2.value = "";
    resultado.textContent = "Resultado: -";
})