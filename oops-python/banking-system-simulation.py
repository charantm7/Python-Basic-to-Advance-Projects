"""
1) user can create a account
 - name, ph-no, random 10 num a/c num, dob, address, age, gender

2) user can check balance with the particular a/c num.

3) user can withdraw and deposit amount

"""


import random

class Account:
  
    def __init__(self, id, name, age, dob):
        self.id = id
        self.name = name
        self.age = age
        self.dob = dob
        self._balance = 0

    def check_balance(self):
        print(f"Balance Amount: {self._balance}")
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Amount {amount} Deposited successfully! ")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficent Balance!")
        else:
            self._balance -= amount
            print(f"Amount {amount} has been withdraw!")


class CurrentAccount(Account):
    
    def withdraw(self, amount):
        limit = 1000
        if amount > self._balance + limit:
            print("You have exceed your limit! Insufficent Balance!")
        else:
            self._balance -= amount
            print(f"Amount {amount} has been withdraw!") 

class SavingsAccount(Account):

    def intrest_rate(self):
        rate = 0.05
        interest = self._balance * rate
        print(f"Intrest for {self._balance} is {interest}")

class Bank:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__database = {}
    
    def display_bank(self):
        return f"welcome to {self.name} at {self.city}"
    
    def creat_account(self, id, name, age, dob, type):
        if type == 'savings':
            new = SavingsAccount(id, name, age, dob)
        elif type == 'current':
            new = CurrentAccount(id, name, age, dob)
        self.__database[id] = new
        print(f"Account created successfully with A/C No {id}!")
        return new
    
    def get_account(self, id):
        return self.__database.get(id, None)
    


def user_creation():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    dob = input("Enter your DOB (D/M/Y): ")
    type = input("Enter the account type (current / Savings): ").lower()
    idd = random.randint(10**9, 10**10 - 1)
    return name, age, dob, idd, type

bank = Bank("SBI Bank", "Bangalore")
bank.display_bank()

while True:
    print("1. Create Account\n2. Your Account\n3. Exit")
    choice = int(input("Enter your choice: "))


    if choice == 1:
        name, age, dob, idd, type = user_creation()
        bank.creat_account(idd, name, age, dob, type)

    elif choice == 2:
        acc = int(input("Enter your 10 digit Account: "))
        account = bank.get_account(acc) 

        if account:
            print(f"Welcome {account.name}! Accessing your account.")

            while True:

                print("1. Check Balance\n2. Deposite\n3. Withdraw\n4. Exit to main menu")
                user_input = int(input("Enter your choice: "))

                if user_input == 1:
                    account.check_balance()
                elif user_input == 2:
                    amt = int(input("Enter the Amount: "))
                    account.deposit(amt)
                elif user_input == 3:
                    amt = int(input("Enter the Amount: "))
                    account.withdraw(amt)
                elif user_input == 4:
                    break
                else:
                    print("Invalid Input!")

        else:
            print("Account Not Found!")

    elif choice == 3:
        break
    else: 
        print("Invalid Input!")

                    

    
    