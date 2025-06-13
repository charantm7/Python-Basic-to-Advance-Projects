def menu():
    print("\n*** Simple Calculator ***\n")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponential\n7.Exit")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        print("Error: Zero Division Error")
    return a/b
def mod(a,b):
    return a%b
def expo(a,b):
    return a**b

def inputs():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a, b

while True:

    menu()
    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Exitin the calculator...")
        break

    if choice in [1,2,3,4,5,6]:
        a,b = inputs()

    if choice == 1:
        print(f"\n{a} + {b} = {add(a,b)}")
    elif choice == 2:
        print(f"\n{a} - {b} = {sub(a,b)}")
    elif choice == 3:
        print(f"\n{a} * {b} = {mul(a,b)}")
    elif choice == 4:
        print(f"\n{a} / {b} = {div(a,b)}")
    elif choice == 5:
        print(f"\n{a} % {b} = {mod(a,b)}")
    elif choice == 6:
        print(f"\n{a} ^ {b} = {expo(a,b)}")
    else:
        print("Invalid choice! Try again..")
    
    

