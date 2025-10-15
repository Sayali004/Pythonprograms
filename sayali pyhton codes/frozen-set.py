fs1 = frozenset([1, 2, 3])
print(fs1) 

fs2 = frozenset((4, 5, 6))
print(fs2) 

fs3 = frozenset({7, 8, 9})
print(fs3) 

fs4 = frozenset("hello")
print(fs4) 

fs5 = frozenset(fs1)
print(fs5) 

a = frozenset([1, 2, 3])
b = a.copy()
print(b)  

c = frozenset([5, 6, 7, 8])
d = frozenset([2, 3, 4, 5])
print(c.union(d)) 
print(c.intersection(d))
print(c.difference(d))
print(c.symmetric_difference(d))
print(c.issubset(d))
print(c.issuperset(d))
print(c.isdisjoint(d))
print(c == d)
print(c | d) 
print(c & d)
print(c - d) 
print(c ^ d) 


