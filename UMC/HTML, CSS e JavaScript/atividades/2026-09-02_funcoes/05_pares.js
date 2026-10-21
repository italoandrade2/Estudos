function* pares() {
    for (let i = 2; i <= 20; i += 2) {
        yield i
    }
}

for (const n of pares()) {
    console.log(n);
}