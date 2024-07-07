print("\n***welcome to number guessing game***\n")

#importing modules random,math for using mathematical operations
import random
import math

#user input for lower and upper range
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

#by using random module and by randint function used to guess the number by the compiler in the given range
x = random.randint(lower, upper)

#total number of guess required to guess the random number of numbers
total_number_of_guess = math.ceil(math.log(upper-lower+1,2))
print(f"\nGuess the number in the given {total_number_of_guess} attempts\n")

#now giving up the try to the user using while loop to guess the number and number of guess attempts
count = 0
flag = False

while count < total_number_of_guess:
    count += 1

    guess = int(input("Enter your guessing number: "))

    if x==guess:
        print(f"\nCongratulations! You guess the number in the {count} attempts\n")
        flag =True
        break

    elif guess > x:
        print("Try again! Your guess is high.\n")

    elif guess < x:
        print("Try again! Your guess is small.\n")

#if the given attempts are reached the game is over and at last to print the number which is guessed by the compiler
if not flag:
    print(f"The number is {x}")
    print(f"You reached your maximum number of {count} attempts! Better luck next time")
