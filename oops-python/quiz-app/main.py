from database_quiz import Quiz

class QuizOperations:

    def __init__(self):
        self.db = Quiz()


    def add_questions(self):
        question = input("Questions: ")
        option = [input(f"Option {i+1}: ")for i in range(4)]
        correct = int(input("Enter correct Option [1,2,3,4]: "))
        self.db.add_question(question, option, correct)
        print("Quetion Added!")

    def logic(self):
        score = 0
        questions = self.db.fetch_question()
        for que in questions:
            print(f"{que[1]}")
            for i in range(2,6):
                print(f"{i-1}. {que[i]}")
            ans = int(input(">> "))
            if ans == que[6]:
                print("CorrecT :)")
                score += 1
            else:
                print(f"Wrong Ans! Correct Ans -> {que[6]}")

        print(f"Your Score is {score}/{len(questions)}")

def main():
    quiz = QuizOperations()

    while True:
        print("---- Welcome To Quize App ----")
        print("1. Add Questions\n2. Start Quize\n3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            quiz.add_questions()

        elif choice == 2:
            quiz.logic()

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()





    

