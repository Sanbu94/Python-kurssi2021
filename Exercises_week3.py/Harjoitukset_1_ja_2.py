# Harjoitus 1
# Suunnittele ja toteuta listan väärinpäin kääntävä algoritmi.
# Algoritmi toimii siis siten, että käännetyn listan ensimmäinen alkio on alkuperäisen listan viimeinen alkio jne.
# Älä käytä list.reverse() funktiota.

# Harjoitus 2
# Suunnittele ja kirjoita algoritmi, joka luo uuden sanan alkuperäisen sanan perusteella siten,
# että alkuperäisestä sanasta otetaan uuteen sanaan joka toinen kirjain.

cars = ["Volvo", "Toyota", "Audi", "Mazda"] 

for car in reversed (cars):
    print(car)


print("\n")


cars = ["Volvo", "Toyota", "Audi", "Mazda"] 

reversed_list = cars[::-1]
print(reversed_list)


print("\n")


sana = "vaalea"

print(sana[1:9:2])

print("\n\n")


# Harjoitus 3:
# Laske montako parillista ja paritonta numeroa listassa (tai tuplessa) on.
# numbers = (3, 1, 6, 3, 4, 7, 0, 6, 3, 2, 6, 8, 3)


numbers = [3, 1, 6, 3, 4, 7, 0, 6, 3, 2, 6, 8, 3]

even_count, odd_count = 0, 0

for num in numbers:
   #even numbers
   if num % 2 == 0:
      even_count += 1
   #odd numbers
   else:
      odd_count += 1
print("Parillisia lukuja on listassa: ", even_count)
print("Parittomia lukuja on listassa: ", odd_count)


print("\n\n")

# Harjoitus 4:
# Pyydä käyttäjää syöttämään sanoja, kunnes käyttäjä syöttää sanan "stop".
# Lopuksi tulosta kaikki käyttäjän syöttämät sanat (paitsi "stop").

sanat = (input("Syötä sanoja: (Lopeta syöttäminen kirjoittamalla 'stop') "))


SANAT = "" 
while sanat != "stop":
    SANAT = SANAT + " " + sanat
    sanat = input("Syötä sanoja: (Lopeta syöttäminen kirjoittamalla 'stop') ")
print ("Syötit sanat:", SANAT)

print("\n\n")

# Harjoitus 5:
# Pyydä käyttäjää syöttämään, monenko luvun keskiarvon tämä haluaa laskea.
# Tämän jälkeen pyydä käyttäjää syöttämään näin monta lukua.
# Laske lopuksi lukujen keskiarvo ja tulosta tämä käyttäjälle
# num = int(input("Syötä numero "))

num = int(input("Kuinka monen numeron keskiarvon haluat laskea:"))
total_sum = 0

for n in range(num):
    numbers = float(input("Syötä numero: "))
    total_sum += numbers

avg = total_sum/num
print("Lukujen keskiarvo on: ", avg)    

