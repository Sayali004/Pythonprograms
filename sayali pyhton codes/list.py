list1 = []
print("Empty list:", list1)

list2 = [1, 2, 3, 4, 5]
print("Integer list:", list2)

list3 = [10, "apple", 3.14, True]
print("Mixed list:", list3)

list4 = list(range(1, 6))
print("List from range:", list4)

list5 = list("hello")
print("List from string:", list5)

list6 = [[1, 2], [3, 4]]
print("Nested list:", list6)

my_list = [10, 20, 30, 40, 50]
my_list.append(60)
print(my_list)

my_list.insert(2, 25)
print(my_list)

my_list.extend([70, 80])
print(my_list)

my_list.remove(25)
print(my_list)

my_list.pop()
print("After pop():", my_list)

print("Index of 40:", my_list.index(40))
print("Count of 20:", my_list.count(20))

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

copied_list = my_list.copy()
print("Copied list:", copied_list)

my_list.clear()
print(my_list)
