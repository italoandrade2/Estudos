# Try e Except 1
# Nome: Italo Andrade Costa
# 17/03/2026 - Versão 1.0

try:
    a = 1 / 0
except ValueError:
    print("Erro de valor")
except NameError:
    print("Erro de nome")
except KeyError:
    print("Erro de Chave")
except:
    print("Erro diferente dos anteriores tratados")
else:
    print("Não houve erros")
finally:
    print("Fim do programa")