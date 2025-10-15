import array

arr1 = array.array('i')  
print("Empty integer array:", arr1)

arr2 = array.array('i', [10, 20, 30, 40, 50])
print("Integer array:", arr2)

arr3 = array.array('i', [-1, -2, -3, 4, 5])
print("Signed integers:", arr3)

arr4 = array.array('I', [10, 20, 30, 40, 50])
print("Unsigned integers:", arr4)

arr5 = array.array('f', [1.5, 2.5, 3.5])
print("Float array:", arr5)

array2 = array.array('i', arr2)
print("Copied array:", array2)
