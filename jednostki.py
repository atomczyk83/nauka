# Kalkulator jednostek

print("Przelicznik centrymentrów na inne jednostki \n\n")

cm = input("Wpisz wartość w cm: ")

# Zmienne dla jednostek

cal = 2.4
metr = 1000
stopa = 30.48

# Tabela

szer = 27
print("-" * szer)
print("|  JEDNOSTKA  |  WARTOŚĆ  |")
print("*" * szer)

# Przeliczenia

print("| {:11s} | {:9.5f} |" .format("CALE", float(cm) / float(cal)))
print("*" * szer)
print("| {:11s} | {:9.5f} |" .format("METRY", float(cm) / float(metr)))
print("*" * szer)
print("| {:11s} | {:9.5f} |" .format("STOPY", float(cm) / float(stopa)))
print("-" * szer)

print("The End Kalkulatora \n\n\n")

# Obliczanie kapitalizacji odsetek

print("Ile zarobisz na lokacie - kalkulator \n\n")

kapital = input("Wpisz wartość kapitału początkowego: ")
oprocentowanie = input("Wpisz wartość oprocentowania rocznego: ")

# Przeliczenia

szer2 = 44
print("-" * szer2)
print("| Lata lokaty | Kwota na koncie |   Zysk   |")
print("-" * szer2)

# Rok 1
rok1 = float(kapital) + float(oprocentowanie) / 100 * float(kapital)

print("| {:11s} | {:15.2f} | {:8.2f} |" .format("1 rok", float(rok1), float(rok1) - float(kapital)))

# Rok 2
rok2 = float(rok1) + float(oprocentowanie) / 100 * float(rok1)

print("| {:11s} | {:15.2f} | {:8.2f} |" .format("2 rok", float(rok2), float(rok2) - float(kapital)))


# Rok 3
rok3 = float(rok2) + float(oprocentowanie) / 100 * float(rok2)

print("| {:11s} | {:15.2f} | {:8.2f} |" .format("3 rok", float(rok3), float(rok3) - float(kapital)))

# Rok 4
rok4 = float(rok3) + float(oprocentowanie) / 100 * float(rok3)

print("| {:11s} | {:15.2f} | {:8.2f} |" .format("4 rok", float(rok4), float(rok4) - float(kapital)))

# Rok 5
rok5 = float(rok4) + float(oprocentowanie) / 100 * float(rok4)

print("| {:11s} | {:15.2f} | {:8.2f} |" .format("5 rok", float(rok5), float(rok5) - float(kapital)))

# The end
print("-" * szer2)
print("Twój zysk wyniesie: ", "{:6.2f}" .format(float(rok5) - float(kapital)), "zł, czyli zarobisz jedno wielkie gówno!!!")
      

