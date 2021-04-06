# -*- coding: utf-8 -*-

# Kalkulator Kalorii dla leniwych panów
print("Witaj w kalkulatorze zapotrzebowania kcal dla panów \n\n")

    # Dane PPM
wzrost = input("Wprowadź swój wzrost w cm: ")
print("Twój wzrost to:", wzrost, "cm")

waga = input("Wprowadź swoją wagę: ")
print("Twoja waga to:", waga, "kg")

wiek = input("Wprowadź swój wiek: ")
print("Twój wiek to:", wiek, "lat")

# Obliczenie dla kobiet - s = -161, dla meżczyzn - s = 5
s = 5

    # Obliczenie PPM
PPM = 10 * int(waga) + 6.25 * int(wzrost) - 5 * int(wiek) + s
print("Współczynnik PMM wynosi:", PPM)


    # Obliczenie zapotrzebowania kalorycznego
print("\nWpisz współczynnik wynikający z trybu życia \n\nPraca siedząca, brak dodatkowej aktywności fizycznej - 1.2, \nLekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu - 1.6, \nPraca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu - 2.0 \n")

wsp = input("Wprowadź współczynnik: ")

print("Współczynnik trybu życia wynosi:", wsp)

print("Twoje dzienne zapotrzebowanie kaloryczne wynosi:", float(wsp) * float(PPM), "kcal")






