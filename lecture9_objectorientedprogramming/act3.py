class Student:
    grade = 10
    name = "Penguine"

    def introduction(self):
        print("Hi, I am a student of CODINGAL.")
    
    def details(self):
        print(f"My name is {self.name}.")
        print(f"I am in grade {self.grade}.")

student_obj = Student()
student_obj.introduction()
student_obj.details()