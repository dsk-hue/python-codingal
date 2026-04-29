class Parrot:
    species = "bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing_and_dance(self):
        print("*bird noises and movements*")

blu = Parrot("blu", 10)
ee = Parrot("ee", 20)
print("{} is {} years old, while {} is {} years old.".format(blu.name, blu.age, ee.name, ee.age))
blu.sing_and_dance()