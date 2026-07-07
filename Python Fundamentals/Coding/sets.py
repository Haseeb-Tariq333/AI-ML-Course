s = {1,2,3,4,4,4,5}
s2 = {4,5,7,8,9}
print(s)
s.add(6)
print(s)
s.remove(1)
print(s)
s.pop()
print(s)
s = s.union(s2)
print(s)
s = s.intersection(s2)
print(s)
s.clear()
print(s)

