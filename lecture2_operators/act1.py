name = "Penguin"
age = 15
is_student = True
weight = 70.5

print("Name:", name)
print("Data type of name:", type(name))

print("Age:", age)
print("Data type of age:", type(age))

print("Is student:", is_student)
print("Data type of is_student:", type(is_student))

print("Weight:", weight)
print("Data type of weight:", type(weight))

print("Some type casting")
age=str(age)
print(age)

weight=int(weight)
print(weight)

print(f"Data type of weight after type casting: {type(weight)}")