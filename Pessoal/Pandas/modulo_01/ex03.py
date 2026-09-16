import pandas as pd

numeros = [10, 20, 30, 40, 50]

s = pd.Series(numeros)

print(s)
print(s.head(1))
print(s.tail(1))
print(len(s))