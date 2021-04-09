# -*- coding: UTF-8 -*-

# deklarujemy i inicjalizujemy zmienne
aktRok = input("Wprowadź aktualny rok: ")
pythonRok = 1989
# obliczamy wiek Pythona
wiekPythona = int(aktRok) - int(pythonRok)

# pobieramy dane
imie = input("Jak się nazywasz? ")
wiek = int(input("Ile masz lat? ")

print("Witaj w moim świecie ",imie)
print("Mów mi Python, mam ",wiekPythona, "lat.")

# instrukcja warunkowa
if wiek > wiekPythona:
	print("Jesteś starszy ode mnie.")
else:
	print("Jesteś młodszy ode mnie.")
