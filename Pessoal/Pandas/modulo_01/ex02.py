import pandas as pd

notas = pd.Series(
    [8.5, 7.0, 9.5, 6.0],
    index=["Python", "SQL", "Git", "HTML"]
    )

print(notas)
print(notas["SQL"])
print(notas["Git"])