# Biblioteca
import locale
locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')

# Entrada
produto = 'Notebook'
quantidade = 10
preco_unitario = 3580.75
custo_total = quantidade * preco_unitario
lucro_percentual = 0.2375   # 23.75%
receita_total = (custo_total * lucro_percentual) + custo_total

# Processamento
relatorio = (
    f"Produto: {produto}\n"
    f"Quantidade vendida: {quantidade}\n"
    f"Preço unitário: {locale.currency(preco_unitario, grouping=True)}\n"
    f"Custo total: {locale.currency(custo_total, grouping=True)}\n"
    f"Margem de lucro: {lucro_percentual:.2%}\n"
    f"Receita total: {locale.currency(receita_total, grouping=True)}"
)

# Saída
linha = "-" * 50
print(linha)
print("RELATÓRIO FINANCEIRO - VENDAS")
print(linha)
print(relatorio)
print(linha)