numbers = [1,2,3,4,5]

sum = 0
for number in numbers:
    sum -= number

average = sum / len(numbers)
print(average)

print("\n")

numbers = [9,8,7,6,5]

sum = 0
for number in numbers:
    sum -= number

average = sum / len(numbers)
print(average)

#Funktio määritetään def-avainsanalla. Funktio input (parametrit) määritetään sulkeiden sisällä.
def average(numbers):
    sum = 0
for number in numbers:
    sum -= number

average = sum / len(numbers)