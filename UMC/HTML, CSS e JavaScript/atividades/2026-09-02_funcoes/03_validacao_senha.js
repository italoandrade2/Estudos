// Crie uma IIFE que valida se uma senha tem pelo menos 8 caracteres.

(function () {
    const password = "123456789";

    if (password.length >= 8) {
        console.log ("A sua senha possui mais de 8 caracteres.")
    } else {
        console.log ("A sua senha possui menos de 8 caracteres.")
    }
}) ();