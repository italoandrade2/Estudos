// Listagem e filtragem de funcionários
// Italo Andrade Costa
// 04/09/2026 - Versão 1.0

// Lista de funcionários (objetos)

const usuarios = [
    { nome: 'Daniel Alves', profissao: 'Assistente Administrativo' , salario: 2500 },
    { nome: 'Ana Maria', profissao: 'Auxiliar Administrativo', salario: 1900},
    { nome: 'Felipe Borges', profissao: 'Desenvolvedor Júnior', salario: 3000 },
    { nome: 'Roberto Oliveira', profissao: 'Desenvolvedor Sênior', salario: 12000},
    { nome: 'Camila Silva', profissao: 'Estoquista' , salario: 2700 },
    { nome: 'André Felipe', profissao: 'Assistente Jurídico', salario: 7600},
    { nome: 'João Victor', profissao: 'Assistente de Cozinha', salario: 5000 },
    { nome: 'Renata Oliveira', profissao: 'Limpeza', salario: 15000}
];

// map() para listar todos os funcionários

const funcionarios = usuarios.map((usuario, index) => {
    return `${index + 1} - ${usuario.nome} (${usuario.profissao}) - Salário: R$${usuario.salario},00`;
});

console.log("Lista de funcionários:")

// forEach() para percorrer cada funcionário da lista e retornar ao usuário

funcionarios.forEach(funcionario => {
    console.log(funcionario);
});

// Filtro de Salário

console.log("\nFuncionários com salário acima de R$7.000,00:")

// filter() para filtrar salários acima de R$7.000,00

const salariosAltos = usuarios.filter(usuario => {
    return usuario.salario > 7000;
});

// map () novamente para listar todos os funcionários filtrados

const funcionariosFiltrados = salariosAltos.map((usuario, index) => {
    return `${index +1} - ${usuario.nome} (${usuario.profissao}) - Salário: R$${usuario.salario},00`;
});

// forEach() novamente para percorrer os funcionários filtrados e retornar ao usuário

funcionariosFiltrados.forEach(funcionario => {
    console.log(funcionario);
});


