# Criar um mini sistema de log com data e hora
# Nome: Italo Andrade Costa
# 21/05/2026 - Versão 1.0

from datetime import datetime

def registrar_log(mensagem, arquivo="sistema.log"):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    entrada = f"[{agora}] {mensagem}\n"
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(entrada)
    print(f"LOG: {entrada.strip()}")

registrar_log("Sistema iniciado")
registrar_log("Usuário 'admin' fez login")
registrar_log("Arquivo alunos.txt modificado")
registrar_log("Sistema encerrado")