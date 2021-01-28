cars = ["Volvo", "Toyota", "Audi", "Mazda"] # Listan määritys.
print(cars)

cars.append("Jeep") # Lisää uuden kohteen listan loppuun.
print(cars)

cars.insert(2, "Fiat",) # Lisää tiettyyn kohtaan uuden.
print(cars)

deleted = cars.pop() # Poistaa viimeisen kohteen.
print(deleted)

deleted = cars.pop(0) # Poistaa määritellyn kohteen.
print(deleted)

cars.clear() # Tyhjentää listan, ei poista sitä

# del cars poistaa listan kokonaan
print(cars)

