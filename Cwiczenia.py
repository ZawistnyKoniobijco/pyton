# iksde = 'Grzegorz strzała'
# print(iksde.replace('rz', 'sz'))

# lmao = 'Grzegorz pała'
# print("pała" in lmao)

# print(10 + 4)
# print(10 - 4)
# print(10 * 4)
# print(10 / 4)
# print(10 // 4)
# print(10 % 4)
# print(10 ** 4)

# <
# <=
# >
# >=
# ==
# != (nie equal)

# and (obie true)
# or (przynajmniej jedna z podanych jest true)
# not (odwraca)

# korale = int(input("Ile masz kilo? "))

# if korale > 100:
#     print("Grubasie")
#     print("Schudnij")
# elif korale > 80:
#     print("No troche schudnij")
#     print("Lol")
# elif korale > 60:
#     print("Jest gucci")
# else:
#     print("Chuj")



# social_points = input("Podaj social score ")

# if int(social_points) < 2137:
#     print("LOL GET GOOD")

# if int(social_points) >= 2137:
#     print("KEEP GOING")


# weight = int(input("Podaj swoją wagę. "))

# weight_pounds = weight * 0.45

# szukanie = input("Kilogramy(K) czy Funty(F)? ")
# if str(szukanie)  == "K":
#     print(str(weight))
# if str(szukanie) == "F":
#     print(str(weight_pounds))


# LOOPS --->

# i = 1
# while i <= 50:
#     print(i)
#     i = i + 1

# i = 1
# while i <= 50:
#     print(i * "*")
#     i = i + 1

# imiona = ["Twój_Stary", "Kran", "Mikser", "Draże", "Cho"]
# imiona[0] = "Lol"  #zamiana pierwszego elementu
# print(imiona[0:3]) #tutaj liczy imiona od pierwszego (0) do trzeciego (2), bo ostatniego (3) nie wlicza

#poniżej dodawanie i odejmowanie elementów z listy w odpowiednich miejscach

# liczby = [1, 2, 3, 4, 5]
# liczby.insert(0, -1) #pierwsze to pozycja, drugie obiekt
# liczby.remove(5)
# liczby.clear() #pozbywa się wszystkie z listy
# print(1 in liczby) #sprawdza czy 1 jest w liście (True or False)
# print(len(liczby)) #sprawdza ile jest elementów w liście
# print(liczby)

#poniżej -> osobne drukowanie itemów z listy (for loop)

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item) #drukuje każdy element z listy osobno

#inna możliwość z while loop

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

#range opcja
# trzecia wartość w pierwszym nawiasie pokzuje o ile będzie skakało wyświetlanie liczb tu 5/7/9
owoce = range(5, 10, 2) #może być tylko 5, wtedy startuje od 0 do 4 albo granice -> tu od 5 do 9
for number in owoce: #to zamaist pokazuwać range deafultowo to drukuje osobno liczby
    print(number)

#może być też

for number in range(5):
    print(number)

#tuples (są niezmienialne po stworzeniu)

warzywa = (1, 2, 3, 3)
warzywa.count(3) #liczy ilość trójek
