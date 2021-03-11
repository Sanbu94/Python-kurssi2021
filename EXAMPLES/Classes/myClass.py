# Yksinkertainen esimerkki luokan määrittämisestä Pythonissa.
class MyClass:
    name = "My Object" # Luokan jäsenmuuttuja. Jäsenmuuttujat määrittävät luokan datan.

    def printName(self): # Parametri "self" viittaa olioon itseensä
        print(self.name)

object1 = MyClass() # Luo olion luokasta MyClass ja tallentaa sen muuttujan object1
object2 = MyClass()




object1.name = "The best object here is!"

print(object1.name)
print(object2.name)