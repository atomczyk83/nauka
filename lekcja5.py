# -*- coding: utf-8 -*-

# Ćwiczenie 1

sentence = "Kurs Pythona jest prosty i przyjemny."
print(sentence)

print(len(sentence))

print(sentence[18:24])

print(sentence[7])
print(sentence[12])
print(sentence[-4])
print(sentence[30])

sentence = sentence[0] + "ó" + sentence[2:28] + "s" + sentence[29:]

print(sentence)

#Ćwiczenie 2

name = input("Jak masz na imię? ")
surname = input("Jak masz na nazwisko? ")
cell = input("Podaj nr swojego telefonu: ")

print("Czy imię to same litery? ", name.isalpha())
print("Czy imię to same cyfry? ", name.isdigit(), "\n")

print("Czy nazwisko to same litery? ", name.isalpha())
print("Czy nazwisko to same cyfry? ", name.isdigit(), "\n")

print("Czy nr tel to same litery? ", name.isalpha())
print("Czy nr tel to same cyfry? ", name.isdigit(), "\n")

name = name.capitalize()
print("Imię: ", name)
surname = surname.capitalize()
print("Nazwisko: ", surname)
cell = cell.replace(" ","")
cell = cell.replace("-","")
print("Nr. telefonu: ", cell)

print("Czy to imię kobiety? ", name.endswith("a"))

personal = name + " " + surname + " " + cell
print(personal)

print(len(personal))

#letters = len(personal) - personal.count(" ") - 9
#print(letters)
#print(len(name + surname))

