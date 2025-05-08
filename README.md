# Python-Basic-to-Advance-Projects

#PROJECT 1: Number Guessing Game.
#Task: Below are the steps:

  Build a Number guessing game, in which the user selects a range.
  Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
  Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
#Analysis:

  Explanation 1: If the User inputs range, let’s say from 1 to 100. And compiler randomly selected 42 as the integer. And now the guessing game started, so the       user entered 50 as his/her first guess. The compiler shows “Try Again! You guessed too high”. That’s mean the random number (i.e., 42) doesn’t fall in the range    from 50 to 100. That’s the importance of guessing half of the range. And again, the user guesses half of 50 (Could you tell me why?). So the half of 50 is 25.      The user enters 25 as his/her second guess. This time compiler will show, “Try Again! You guessed too small”. That’s mean the integers less than 25 (from 1 to      25) are useless to be guessed. Now the range for user guessing is shorter, i.e., from 25 to 50. Intelligently! The user guessed half of this range, so that, user   guessed 37 as his/her third guess.  This time again the compiler shows the output, “Try Again! You guessed too small”. For the user, the guessing range is          getting smaller by each guess. Now, the guessing range for user is from 37 to 50, for which the user guessed 43 as his/her fourth guess. This time the compiler     will show an output “Try Again! You guessed too high”. So, the new guessing range for users will be from 37 to 43, again for which the user guessed the half of     this range, that is, 40 as his/her fifth guess.  This time the compiler shows the output, “Try Again! You guessed too small”. Leaving the guess even smaller such   that from 41 to 43. And now the user guessed 41 as his/her sixth guess. Which is wrong and shows output “Try Again! You guessed too small”. And finally, the User   Guessed the right number which is 42 as his/her seventh guess.

Formula:
So, the minimum number of guesses depends upon range. And the compiler must calculate the minimum number of guessing depends upon the range, on its own. For this, we have a formula:-

 Minimum number of guessing = log2(Upper bound – lower bound + 1)

 #Step-by-step algorithm:

  User inputs the lower bound and upper bound of the range.
  The compiler generates a random integer between the range and store it in a variable for future references.
  For repetitive guessing, a while loop will be initialized.
  If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
  Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
  And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
  Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.


#PORJECT 2: HANGMAN GAME!

#Step 1: Importing Required Modules
>random: This module is used to generate random selections, such as picking a word from the 
 list.
>Counter: A class from the collections module that counts the occurrences of elements in an 
 iterable, such as the letters in a string.

#Step 2: Defining the List of Device Names.
>device_names: This is a string containing names of various computer components, separated by spaces.
some_words = device_names.split(): The split() method converts the string into a list of individual device names. Each name becomes an element in the list.
word = random.choice(some_words): A random word is selected from the some_words list. This is the word the player will try to guess.

#Step 3: Greeting the Player.
>The player is asked to input their name.
The program greets the player by name and welcomes them to the game.

#Step 4: Initializing Variables.
>guessed_letters: A string that will store the letters the player has guessed. It's initialized with a space.
>chances = len(word) + 2: The number of chances the player has is set to the length of the word plus 2 extra chances. This gives the player a bit more room to make mistakes.
>print("_" * len(word)): The program prints a series of underscores equal to the length of the word, representing the unguessed letters.
>flag: A boolean flag that indicates whether the word has been completely guessed (True) or not (False).
>playing: This variable is initialized as True, but it is not used in the rest of the program.

#Step 5: Main Game Loop.
>The loop runs as long as the player has chances left and hasn't guessed the word (flag is False).
The player is prompted to enter a letter, which is converted to lowercase.

#Step 6: Input Validation.
>isalpha(): Ensures the player enters a letter of the alphabet.
If the input is not a letter, the program asks the player to enter only alphabets and continues to the next iteration of the loop.
>len(guess) > 1: Ensures that the player enters only a single letter.
If the player enters more than one letter, the program asks them to enter only a single letter and continues.
>guess in guessed_letters: Checks if the player has already guessed that letter.
If the player repeats a guess, the program informs them and continues.

#Step 7: Updating Guessed Letters.
>The guessed letter is added to the guessed_letters string.

#Step 8: Displaying the Word with Guessed Letters.
>The program iterates through each character in the randomly selected word (word).
If the character has been guessed (i.e., it's in guessed_letters), the program prints the character.
If the character hasn't been guessed yet, the program prints an underscore (_).
The end=" " argument in the print() function ensures that the characters are printed on the same line with a space between them.

#Step 9: Checking if the Word is Fully Guessed.
>Counter(guessed_letters) & Counter(word): This operation creates a Counter object that includes only the letters in word that have been guessed.
If this Counter object matches the Counter object of the original word, it means that all the letters in the word have been guessed correctly.
If the word is fully guessed, the program congratulates the player, sets flag to True, and breaks out of the loop, ending the game.

#Step 10: Reducing Chances.
>Each time the player makes a guess, the number of remaining chances is reduced by 1.

#Step 11: Handling Game Over.
>After the loop ends, if the player hasn't guessed the word (i.e., flag is still False), the program informs the player that they have lost the game and reveals the correct word.

#Step 12: Handling Keyboard Interrupts.
>This try-except block catches a KeyboardInterrupt (e.g., when the player presses Ctrl + C).
If the program is interrupted, it prints "Invalid Input" and exits gracefully.
