# Operadores "+" e "*" com strings
# Nome: Italo Andrade Costa
# 05/03/2026 - Versão 1.0

# Montando um Crachá
nomec = "Carlos Eduardo"
linhac = "*" * (len(nomec) + 6)
print(linhac)
print("*  " + nomec + "  *")
print(linhac)

# Email Corporativo
# Entrada
linhae = "=" * 50
nomee = "Luiz"
sobrenome = "Santos"
# Processamento
email = nomee.lower() + "." + sobrenome.lower() + "@empresa.com"
# Saída
print(linhae)
print("E-mail corporativo:", email)
print(linhae)