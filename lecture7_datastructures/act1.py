lst=["apple", "orange", "banana", "strawberry", "kiwi"]

print(len(lst))

print(lst[-1])

lst.append("mango")
print(lst)

lst.remove("mango")
print(lst)

lst.insert(2, "mango")
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)

print(lst*2)

print(lst[1:3])

new_lst=lst.clear()
print(new_lst)
