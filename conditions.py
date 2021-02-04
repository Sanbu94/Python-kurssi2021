a = 10 # Arvon sijoitus muuttujaan
b = 20

# Vertailuoperaattoreita   
# == Yhtäsuuruusvertailu

if a == b: # Onko a yhtä suuri kuin b?
    print(a, "equals", b)
else:
    print(a, "does not equal", b) # sep-parametrillä voidaan määrittää print-funktion käyttämä erotinmerkki    

# != Erisuuruusvertailu
if a != b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

if not a == b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)


# < pienempi kuin, > suurempi kuin
if a < b:
    print(a, "is less than", b)
elif a > b:
     print(a, "is greater than", b)
else:
    print(a, "equals", b)  

# Vertailun tulos voidaan tallentaa muuttujaan
result = a == b
print(result)    

if result:
    print(a, "equals", b)  
else:
    print(a, "does not equal", b)

# Python ei tue switch-case rakennetta
       