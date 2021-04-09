# Ćwiczenie 1

#lista = []

#while True:
 #   liczba = input("Wpisz liczbę całkowitą dodatnią: ")
  #  liczba = int(liczba)
  #  if liczba >= 0:
  #      lista.append(liczba)
   #     continue
   # elif liczba < 0:
  #      print("Suma podanych liczb: ", sum(lista))
   #     print("Ilość podanych liczb: ", len(lista))
    #    break


# Ćwiczenie 2

#print("Mamy listę elementów: ", [5,6,7,8])
#for liczba in [5,6,7,8]:
#    print("element listy: ", liczba)


# Ćwiczenie 3

#liczby = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#print("Lista elementów: ", liczby)

#for nr in liczby:
#    print(nr)

#print("Suma: ", sum(liczby))


# Ćwiczenie 4 - silnia

silnia = input("Wprowadź dodatnią liczbę całkowitą: ")
silnia = int(silnia)
a = 1 #zmienna pomocnicza

if silnia in (0,1):
    print("1")  #dlaczego drukuje 2x????

elif silnia > 1:
    for i in range(2, silnia+a): #dlaczego w ogóle drukuje??
        a = a*i


# Ćwiczenie 5



print(a)

