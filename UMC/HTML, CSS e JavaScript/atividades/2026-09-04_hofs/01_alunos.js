const alunos = [
    { nome: "Ana", nota: 8.5 },
    { nome: "Bruno", nota: 4.2 },
    { nome: "Carla", nota: 9.0 },
    { nome: "Diego", nota: 5.5 },
];


console.log("Alunos aprovados:")

const aprovados = alunos
    .filter(a => a.nota > 6)
    .map(a => {return `Nome: ${a.nome} - Nota: ${a.nota}`})

aprovados.forEach(a => {
    console.log(a)
})

console.log("\nMédia da Turma:")

const soma = alunos
    .map(a => a.nota)
    .reduce((soma, a) => soma + a, 0);
console.log(soma / alunos.length);


console.log("\nTodos foram aprovados?")

const todosAprovados = alunos
    .every(a => a.nota >= 6);

console.log(todosAprovados)


console.log("\nMaior nota:")

const maiorNota = [...alunos]
    .sort((a, b) => b.nota - a.nota)[0];

console.log(`Nome: ${maiorNota.nome} - Nota: ${maiorNota.nota}`)