# set alustetaan {} syntaksilla. Set on järjestämätön tietorakenne, 
# eli sen sisällön järjestys voi muuttua aina, kun sinne lsiätään tai poistetaan dataa.
units = {"tank", "plane", "ship"} 
print(units)

#Set:iin voi lisätä dataa add-funktiolla.
units.add("soldier")
print(units)

#Set ei salli duplikaattiarvoja.
units.add("soldier")
print(units)

unitList = ["tank", "plane", "ship", "soldier", "soldier", "soldier"]
print(unitList)
# Muunnetaan lista set:ksi ja takaisin listaksi. Tämä poistaa duplikaatit(koska set ei tue niitä).
unitList = list(set(unitList))
print(unitList)

# Set:iin voi lisätä kerralla useamman alkion.
units.update(["heavy tank", "helicopter"])
print(units)

# Set:stä voi myös poistaa alkioita
units.discard("soldier")
units.discard("soldier")
print(units)

units.remove("tank")
print(units)

# Myös pop toimii set:lle
random = units.pop()
print(random)

print(units)