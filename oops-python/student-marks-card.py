class Student:
    def __init__(self, name, roll_no, contact):
        self.name = name
        self.roll_no = roll_no
        self.contact = contact
        self.marks = {}
        
    def add_marks(self, sub, mark):
        return self.marks[sub] == mark

    def calc_avg(self):
        total = 0
        for value in self.marks.values():
            total += value
        avg = total/len(self.marks)
        print(f"{self.name}'s marks average is {avg}.")
        
    def is_pass(self):
        failed = any( mark<35 for mark in self.marks.values())
        if failed == True:
            print(f"{self.name} has Failed!")
        else:
            print(f"{self.name} has passed in all subjects :)")

    def status_validation(self, mark):
        if mark > 35:
            return 'Pass'
        else:
            return 'Fail'

    def failed_sub(self):
        fail_sub = {}
        for sub, mark in self.marks.items():
            if mark < 35:
                fail_sub[sub] = mark
        for sub, mark in fail_sub.items():
            print(f"{self.name} has failed in {sub} and got {mark}/100 ):")

    def grade_persub(self, mark):
        
        if mark > 90:
            return 'A++'
        elif mark > 80:
            return 'A'
        elif mark > 70:
            return 'B'
        elif mark > 60:
            return 'c'
        elif mark > 50:
            return 'D'
        else:
            return 'E'
        
    def total_grade(self):
        percentage = self.calc_avg()*100
        if percentage > 90:
            return 'A++'
        elif percentage > 80:
            return 'A'
        elif percentage > 70:
            return 'B'
        elif percentage > 60:
            return 'c'
        elif percentage > 50:
            return 'D'
        else:
            return 'E'
        


class Report:
    def __init__(self):
        self.report = {}
        self.student = {}              

    def add_student(self, name, roll_no, contact):
        self.student = Student(name,roll_no, contact)
        print(f"{name} has been added as a student successfully!")
        
    
    def marks_input(self, sub, marks):
        student_marks = self.student.add_marks(sub, marks)
        return student_marks
    
    """
    ----- SSLC Marks Report -----

    ** Student Details **

    Name : Charan T M
    USN : 1VE23CS000
    Contact : 6362218365

    ** Student Marks Report **

    |  Subject  |  Marks  |  Grade  |  Status  |
    |  Maths    |  100    |  A++    |  Pass    |
    |  Python   |  90     |  A      |  Pass    |
    |  Java     |  80     |  B      |  Pass    |

    Total Marks : 270 / 300
    Percentage : 95%
    Grade : A++

    ** Thank You **

    """
    
    def generate_report(self):
        print("\n----- Student Marks Report -----\n")
        print("** Student Details **\n")
        print(f"Name : {self.student.name}")
        print(f"USN : {self.student.roll_no}")
        print(f"Contact : {self.student.contact}")
        print("\n** Student Marks Record **\n")
        print("Subjects\tMarks\tGrade\tStatus")
        total = 0
        no_of_sub = 0*100

        for sub, mark in self.student.marks.items():
            total += mark
            no_of_sub += 1
            print(f"{sub}\t{mark}\t{self.student.grade_persub(mark)}\t{self.student.status_validation(mark)}")
        
        print(f"\nTotal Mark : {total}/{no_of_sub}")
        print(f"Percentage : {self.student.calc_avg()*100}")
        print(f"Grade : {self.student.total_grade()}")

        print("\n** Thank You **")

            




    




