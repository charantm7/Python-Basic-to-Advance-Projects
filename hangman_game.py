import random
from collections import Counter

device_names = "ram rom networkcard gpu coolingfan mothercard sourcecontrol instructionpanel cpu"

some_words=device_names.split()
word = random.choice(some_words)


name = input("Name Please: ")
print(f"Hey {name}! Welcome to the hangman game")
print("I hope you'll enjoy it")
print()

    #sorting the letters guessed by user
guessed_letters= " "
chances= len(word)+2
print(f"No of chances to guess is {chances}")
print("_"*len(word))
flag = False
playing = True

try:
    while chances>0 and  not flag:
        print()
        guess = input("Enter the guessing letter: ").lower()

        if not guess.isalpha():
            print("Enter only alphabets!")
            continue

        elif len(guess)>1:
            print("Enter only single letter!")
            continue
            
        elif guess in guessed_letters:
            print("The letter guessed is alredy guessed!")
            continue

        guessed_letters += guess

        for char in word:
            if char in guessed_letters:
                print(char,end=" ")
            else:
                print("_",end=" ")
        print()

        if Counter(guessed_letters) & Counter(word) == Counter(word):
            print("congratulation! You won.")
            flag = True
            break

        chances -= 1

    if not flag:
        print("You lost the game!") 
        print(f"The word is {word}")

except KeyboardInterrupt:
    print()
    print("Invalid Input")


        
