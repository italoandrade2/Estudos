import pandas as pd

vendas = pd.DataFrame({
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Headset", "SSD", "Webcam", "RAM"],
    "categoria": ["Informática", "Periféricos", "Periféricos", "Informática", "Periféricos", "Componentes", "Periféricos", "Componentes"],
    "quantidade": [2, 20, 15, 5, 12, 8, 18, 25],
    "preco": [3500, 80, 120, 900, 250, 400, 180, 300]
})

print(vendas[vendas["quantidade"] > 10])                                # Mouse (20), Teclado (15), Headset (12), Webcam (18), RAM (25)
print(vendas[vendas["preco"] > 500])                                    # Notebook (3500) e Monitor (900)
print(vendas[(vendas["quantidade"] > 10) & (vendas["preco"] > 100)])    # Teclado (15, 120), Headset (12, 250), Webcam (18, 180) e RAM (25, 300)
print(vendas[(vendas["quantidade"] > 15) | (vendas["preco"] > 1000)])   # Mouse (20), Webcam (18) e RAM (25) | Notebook (3500)
print(vendas[~(vendas["categoria"] == "Periféricos")])                  # Notebook (Informática), Monitor (Informática), SSD (Componentes) e RAM (Componentes)