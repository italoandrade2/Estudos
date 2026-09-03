// async / await
// Italo Andrade Costa
// 02/09/2026 - Versão 1.0

async function buscarDados() {
    return "dados carregados";
}

async function exemplo() {
    const resultado = await buscarDados();
    console.log(resultado);
}

exemplo();