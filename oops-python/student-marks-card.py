
"""
    Example Report Template

    ----- Student Marks Report -----

    ** Student Details **

    Name : Charan T M
    USN : 1VE23CS036
    Contact : 6362218372

    ** Student Marks Record **

    Subjects  Marks   Grade   Status  
    MATHS     89      A       Pass    
    PYTHON    76      B       Pass    
    JAVA      80      B       Pass    
    MC        90      A       Pass    
    ADA       86      A       Pass    

    Total Mark : 421/500
    Percentage : 84.000
    Grade : A

    ** Thank You **

    """

class Student:
    def __init__(self, name, roll_no, contact):
        self.name = name
        self.roll_no = roll_no
        self.contact = contact
        self.marks = {}
        
    def add_marks(self, sub, mark):
        self.marks[sub] = mark

    def calc_avg(self):
        total = 0
        for value in self.marks.values():
            total += value
        avg = total//len(self.marks)
        return avg
        
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
        percentage = self.calc_avg()
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
        
    
    def marks_input(self, n):
        student = self.student
        for i in range(n):
            sub = input("Subject: ")
            marks = int(input("Marks: "))
            student.add_marks(sub, marks)
        
    
    def generate_report(self):
        student = self.student
        print("\n----- Student Marks Report -----\n")
        print("** Student Details **\n")
        print(f"Name : {student.name}")
        print(f"USN : {student.roll_no}")
        print(f"Contact : {student.contact}")
        print("\n** Student Marks Record **\n")
        print(f"{'Subjects':<10}{'Marks':<8}{'Grade':<8}{'Status':<8}")
        total = 0
        no_of_sub = 0

        for sub, mark in student.marks.items():
            total += mark
            no_of_sub += 1
            print(f"{sub:<10}{mark:<8}{student.grade_persub(mark):<8}{student.status_validation(mark):<8}")
        
        print(f"\nTotal Mark : {total}/{no_of_sub*100}")
        print(f"Percentage : {student.calc_avg():.3f}")
        print(f"Grade : {student.total_grade()}")

        print("\n** Thank You **")


print("\n--- Welcome to Student Marks Report Generator ---\n")

name = input("Enter the name: ")
roll = input("Enter Roll Number: ")
contact = int(input("Enter contact details: "))
report = Report()
student = report.add_student(name, roll, contact)
n = int(input("Enter number of subjects: "))
report.marks_input(n)

report.generate_report()

