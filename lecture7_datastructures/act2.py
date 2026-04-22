my_dict = {}

my_dict = {
    "a": 1,
    2 : "GOOGLE",
    3 : "META",
    4 : {1, 2, 3}
}

print(my_dict[2])
print(my_dict["a"])
print(my_dict[4])

my_dict[2] = "AMAZON"
print(my_dict[2])

del my_dict[4]
print(my_dict)

my_dict.pop(2)
print(my_dict)

my_dict.clear()
print(my_dict)