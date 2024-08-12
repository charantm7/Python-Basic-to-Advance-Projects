def lose():
    print("\nBad luck!Try again later.")
    exit(0)

def consecutive(numbers):
    i = 1
    while i<len(numbers):
        if numbers[i] != (numbers[i-1]+1):
            return False
        i = i+1
    return True

def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near
    
def game():
    numbers = []
    last = 0

    while True:
        print("\nFor first turn enter 'F', for second turn ente 'S':")
        inp = input('>').lower()

        if inp == 'f':
            while True:

                if last == 20:
                    lose()
                print("\nHow many numbers you want enter b/w (1-3):")
                user = int(input('>'))

                if 1 <= user <= 3:
                    comp = 4- user
                    print("\nEnter your values!:")
                    for i in range(user):
                        numbers.append(int(input('>')))


                    last = numbers[-1]

                    if consecutive(numbers) == True:
                        if last == 21:
                            lose()
                        
                    
                        else:
                            print("\nComputer turn")
                            j = 1
                            while j<=comp:
                                numbers.append(last+j)
                                j = j+1
                            last = numbers[-1]

                            print(f"Consecutive sequence is{numbers}")
                    else:
                        print("\ninput consecutive integers")
                        lose()



                else:
                    print("Enter the number b/w (1-3)")
                    lose()

        elif inp == 's':
            comp = 1
            last = 0
            print("Computer Turn!")
            while last <20:
                j = 1
                while j<=comp:
                    numbers.append(last+j)
                    j = j+1
                last = numbers[-1]
                print(f"\nconsecutive sequence is {numbers}")
                
                if last == 21:
                    lose()

                else:
                    print("\nYour turn!")
                    print("\nHow many numbers you want to enter b/w (1-3)")
                    user = int(input('>'))

                    print("\nEnter the values!")
                    for i in range(user):
                        numbers.append(int(input('>')))

                    if consecutive(numbers) == True:
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        
                        print ("\nYou did not input consecutive integers.")
                        lose()
                        

                    last = numbers[-1]

            print("\nCongratulation! You won")
            exit(0)

        else:
            print("\nInvalid! Enter only 'F' or 'S'")

while True:
    print("\nDo you want to play this game(Yes/No)")
    val = input('>').lower()

    if val == 'yes':
        game()

    else:
        print("\nDo you want to exit the game (Yes/No)")
        vall = input('>').lower()
        
        if vall == 'yes':
            print("\nYou are quiting the game!")
            exit(0)

        elif vall == 'no':
            print("Continuing...")

        else:
            print("Invalid choice")



