from enums import Choice
import random

class Player():
    def __init__(self, name):
        self.name = name


    def play(self):
        return None


class HumanPlayer(Player):
    def play(self):
        #Käyttäjän valinta tallennetaan tähän muuttujaan.
        choice = Choice.NONE

        while choice == Choice.NONE:
            try:
                choiceInt = int(input("Give your choice (1=Rock", "2=Paper", "3=Scissors): "))
                choice = Choice(choiceInt)
            except ValueError:
                print("Illegal input, give a number between 1 and 3")
                choice = Choice.NONE
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                print("Unknown error!")
        return choice


class CPUPlayer(Player):
    def play(self):
        return Choice(random.randint(1,3))

        
