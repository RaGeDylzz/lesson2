import random

numberEntered = int(input("Enter a number from 1-12(while loop): "))
count = 1
while count <= 12:
    print(count, "x", numberEntered, "=", count * numberEntered)
    count = count + 1

print("Finished while loop...")


for x in range(100):
    print()


def ask_question():
    random_number = random.randint(1, 13)
    answer_input = int(input("What is " + str(random_number) + " x " + str(numberEntered) + "? "))
    if answer_input == random_number * numberEntered:
        print("You have gotten it right well done!")
        return True
    else:
        print("Incorrect!")
        return False


correct_answers = 0
for i in range(5):
    if ask_question():
        correct_answers = correct_answers + 1


print("You got", correct_answers, "out of 5")

