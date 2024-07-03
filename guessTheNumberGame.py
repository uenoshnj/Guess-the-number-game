import random

# Function: Make answer number
def makeAnswer(firstNumber, secondNumber):
    if firstNumber == secondNumber:
        answer = firstNumber
    elif firstNumber < secondNumber:
        answer = random.randint(firstNumber, secondNumber)
        print(f"The answer is a number between {firstNumber} and {secondNumber}")

    else:
        answer = random.randint(secondNumber, firstNumber)
        print(f"The answer is a number between  {secondNumber} and {firstNumber}")
    return answer

# game start
print("Let's start guess the number game!\n")

firstNumber = int(input("Please enter the first number!\n"))

print(f"first number is : {firstNumber}\n")

secondNumber = int(input("Please enter the second number!"))
print(f"second number is : {secondNumber}\n")

answer = makeAnswer(firstNumber, secondNumber)

# Repeat until guess the correct answer.
while True:
    guessNumber = int(input("Please enter guess number!\n"))
    if answer == guessNumber:
        print(f"Correct! The answer is {guessNumber}!\n")
        break

