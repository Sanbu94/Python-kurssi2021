# Dictionary sisältää avain-arvo -pareja. Avaimien on oltava yksilöllisiä. Arvoja indeksoidaan avaimilla.
carInfo = {
    "brand": "Toyota", 
    "model": "Corolla",
    "year": 2010, 
    "price": 5000.50
}

print(carInfo)

# Arvon lisäys dictionaryyn.
carInfo["color"] = "red"
print(carInfo)

carInfo["year"] = 2015
print(carInfo)

# Datan tallenus muuttujaan
price = carInfo["price"]
print(price)

# Avain-arvo -parit poistetaan pop-funktiolla. Jos avainta ei löydy, palautetaan oletusarvo, jos sellainen on
# on välitetty funktiolle parametrinä. Jos ei ole välitetty, Python nostaa virheen.
color = carInfo.pop("color")
print(color)

color = carInfo.pop("color","N/A")
print(color)

