class Student:
    grade = 9
    #constructor-used to initialize something
    def __init__(self, name):

    def display(self):
        print(f"Dharshini is in {self.grade}th grade")
st1 = Student()
print(st1.grade)
st1.display()