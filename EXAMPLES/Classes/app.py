from phonebook import Phonebook
from contact import Contact


def main():
    phonebook = Phonebook()

    person1 = Contact("Maija", "Mehiläinen", "29392949", 1994)
    person2 = Contact("Matti", "Meikäläinen", "03846737", 1995)

    phonebook.AddContact(person1)
    phonebook.AddContact(person2)

    phonebook.PrintContacts()

if __name__ == "__main__":
    main()