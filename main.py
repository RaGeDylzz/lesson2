# Times tables etc
import random

# number = int(input("Enter a number from 1-12 (for loop): "))
#
# for i in range(1, 13):
#     print(i, "x", number, "=", i * number)
#
# print("Finished for loop...")
# print()

numberEntered = int(input("Enter a number from 1-12(while loop): "))
count = 1
while count <= 12:
    print(count, "x", numberEntered, "=", count * numberEntered)
    count = count + 1

print("Finished while loop...")


for x in range(100):
    print()

randomNumber = random.randint(1, 13)
isIncorrect = True
while isIncorrect:
    answer = int(input("What is " + str(randomNumber) + " x " + str(numberEntered) + "? "))
    if answer == randomNumber * numberEntered:
        print("You have gotten it right well done!")
        isIncorrect = False
    else:
        print("No! Try again.")
