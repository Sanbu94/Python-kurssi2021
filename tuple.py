phones = ("Nokia", "Apple", "Samsung")
print(phones)

# Palauttaa alkion indeksistä 1 ja tallentaa sen muuttujaan phone
phone = phones[1] 
print(phone)

# Palauttaa alkion indeksistä 1 ja tallentaa sen muuttujaan phone
phone = phones[2] 
print(phone)

# Muuttaa tuplen listaksi, jotta sitä voi muuttaa (lisätä uusia alkioita)
phoneList = list(phones) 
phoneList.append("OnePlus")
phones = tuple(phoneList)

print(phones) 

