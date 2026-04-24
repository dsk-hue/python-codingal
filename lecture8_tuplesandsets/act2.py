a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.union(b)
print(a | b)
print(c)

d = a.intersection(b)
print(a & b)
print(d)

#difference; the parts in a that aren't in b
e = a.difference(b)
print(a - b)

f = c - d
print(c ^ d)
print(f)
