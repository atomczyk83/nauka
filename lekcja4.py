print("Lista moich ulubionych seriali\n")

tvshows = {
"Nasza planeta" : 8.99, 
"Czernobyl" : 8.73, 
"Gra o tron" : 8.46, 
"Breaking Bad" : 8.35, 
"Kompania Braci" : 8.21, 
"Rick i Morty" : 7.99, 
"Biuro" : 7.65, 
"Ostatni taniec" : 7.23, 
"Sherlock" : 6.98, 
"Peaky Blinders" : 6.53
}

print(list(tvshows.keys()))
print("********************************************\n")
name = input("Jaki serial chcesz obejrzeć? ")
print("Serial {} otrzymał ocenę {}." .format(name, tvshows[name]))

print("********************************************\n")
new = input("Jaki serial chcesz dodać do bazy? ")
rating = input("Jaką ocenę wystawiasz serialowi " + new + "? ")

tvshows[new] = float(rating)

print("********************************************\n")

print("Nowa lista:\n")
print(list(tvshows.keys()))
