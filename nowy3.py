# -*- coding: UTF-8 -*-

op = "t"
while op == "t":
    a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(" ")
    
    print("Wprowadzono liczby: {}, {}, {}" .format(a,b,c))

    if a < b:
        if a < c:
            print("Najmniejsza: ", a)
        elif b < c:
            print("Najmniejsza: ", b)
        else:
            print("Najmniejsza: ", c)
       
    op = input("Jeszcze raz (t/n)? ")

print("Nara...")
