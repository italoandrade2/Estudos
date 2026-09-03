# Código ANSI para cor no Python
# Nome: Italo Andrade Costa
# 05/03/2026 - Versão 1.0

#\033[style; text; back m
COR = '\033[1;33;41m'
Fim = '\033[0m'
imp = "MEU TEXTO A SER IMPRESSO"
print(f' {COR} {imp} {Fim}')