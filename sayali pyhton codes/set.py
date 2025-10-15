my_set = {1, 2, 3}
print(my_set)
my_set.add(4)
print(my_set)
my_set.remove(4)
print(my_set) 
my_set.discard(4)
print(my_set) 
item = my_set.pop()
print(item)
print(my_set)
my_set.clear()
print(my_set)

my_set2 = set([1, 2, 3])
print(my_set2)
set2 = my_set2.copy()
print(set2)

my_set3 = set((1, 2, 3))
print(my_set3)  

my_set4 = set("hello")
print(my_set4) 

my_set5 = set()
print(my_set5)
my_set5.add(1)
print(my_set5)

my_set6 = {1, "hello", 3.14, (1, 2)}
print(my_set6)

a = {1, 2}
b = {2, 3}
print(a.union(b)) 
print(a | b)
print(a.intersection(b)) 
print(a & b) 
print(a.difference(b))
print(a - b)  
print(a.symmetric_difference(b))  
print(a ^ b)
print(a.issubset(b)) 
print(a.issuperset(b)) 
print(a.isdisjoint(b))
print(a.isdisjoint({4, 5})) 

