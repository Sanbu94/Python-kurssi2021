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


sana = "ikkuna"

print(sana[1:9:2])

