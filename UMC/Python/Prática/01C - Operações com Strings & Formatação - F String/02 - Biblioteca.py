import locale
valor = 1768
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
valor = locale.currency(valor, grouping=True, symbol=True)
print(valor)