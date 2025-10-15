import array

arr = array.array('i', [10, 20, 30, 40, 50])
print("Original Array:", arr)

arr.append(60)
print("After append(60):", arr)

arr.insert(2, 25)  
print("After insert(25) at index 2:", arr)

arr.remove(40)
print("After remove(40):", arr)

arr.pop(3)
print("After pop at index 3:", arr)

print("Index of 50:", arr.index(50))
print("Element at index 1:", arr[1])

arr.reverse()
print("After reverse:", arr)

print("Count of 20:", arr.count(20))

arr2 = array.array('i', [70, 80, 90])
arr.extend(arr2)
print("After extend with arr2:", arr)

print("Array length:", len(arr))
