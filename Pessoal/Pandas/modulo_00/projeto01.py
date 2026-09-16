# Importa a biblioteca do Pandas
import pandas as pd

# Transforma os dados da tabela em Dicionário em um DataFrame
vendas = pd.DataFrame ({
    "data": ["2026-07-25", "2026-07-26", "2026-07-26", "2026-07-28", "2026-08-02", "2026-08-03", "2026-08-03", "2026-08-03", "2026-08-05", "2026-08-10"],
    "produto": ["SSD 512GB", "HD 1TB", "Cooler", "RTX3060 12GB", "SSD 1TB", "Pendrive 64GB", "Poco X6", "Controle Dualsense PS5", "Headset Redragon", "PlayStation 4"],
    "categoria": ["Hardware", "Hardware", "Hardware", "Hardware", "Hardware", "Acessórios", "Celulares", "Acessórios", "Acessórios", "Consoles"],
    "quantidade": [3, 2, 1, 1, 2, 4, 1, 2, 1, 1],
    "preco": [600.99, 550.99, 1200.00, 2459.99, 985.99, 68.99, 1700.50, 450.00, 320.50, 1899.99],
    "vendedor": ["Flávio", "Flávio", "Flávio", "Flávio", "Flávio", "Paulo", "Júlia", "Paulo", "Paulo", "Márcia"]
})

print(vendas)
print(pd.__version__)
print(vendas.dtypes)