# Funktio määritetään def-avainsanalla. Funktio input (parametrit) määritetään sulkeiden sisällä.
# Muuttujan tyypin voi määrittää parametrille, mutta tulkki ei määrityksestä välitä, vaan
# päättelee tyypin ajon aikana. Tyyppimääritys on vain vihje ohjelmoijalle.
isAverageRun = False

# Pythonissa voimme määrittää vain yhden tietyn nimisen funktion. Funktioiden overloadaus
# ei ole mahdollista.
# Parametrille voidaan määrittää oletusarvo, esim. printResult=True.
def average(numbers, printResult: bool = True):
    result = 0
    
    # global avainsanan avulla voimme muuttaa globaalin muuttujan arvoa funktion sisällä.
    global isAverageRun

    for number in numbers:
        result += number
    average = result / len(numbers)

    if printResult:
        print(average)

    # Funktio muuttaa ohjelman tilaa, sillä on siis ns. sivuvaikutuksia.
    isAverageRun = True
    print(isAverageRun)
    
    return average

# Summan laskeva funktio. Ottaa vastaan määrittelemättömän määrän parametrejä.
def sum(*numbers):
    result = 0
    for numbers in numbers:
        result += numbers
    return result


def main():
    numbers = [1,2,3,4,5]
    avg = average(numbers)
    print(isAverageRun)

    numbers = [9,8,7,6,5,2,9,4,5,2]
    avg = average(numbers, False)


    summa = sum(1,2,3,4,5,6,7,8)
    summa2 = sum()
    print(summa, end="\t")
    print(summa2, end="\t")
    print()

# Tapa toteuttaa main-funktio Pythonissa.
# Määritetään kaikki muu koodi paitsi alla oleva ja globaalit funktioden sisällä.
if __name__ == "__main__":
    main()