import random
import time

number_entered = int(input("Enter a number from 1-12: "))
count = 1
while count <= 12:
    print(count, "x", number_entered, "=", count * number_entered)
    count = count + 1

print()
for x in range(3, 0, -1):
    time.sleep(1)
    print(x, "... ", end="")


time.sleep(1.2)


for x in range(50):
    print()


correct_answers = 0
for i in range(5):
    random_number = random.randint(1, 12)
    answer_input = int(input("What is " + str(random_number) + " x " + str(number_entered) + "? "))
    if answer_input == random_number * number_entered:
        print("You got it right well done!")
        correct_answers = correct_answers + 1
    else:
        print("Incorrect!")


print("You got", correct_answers, "out of 5")

