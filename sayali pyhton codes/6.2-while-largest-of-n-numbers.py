n = int(input("Enter the number of elements: "))
largest = None
count = 0
while count < n:
    num = int(input("Enter a number: "))
    if largest is None or num > largest:
        largest = num
    count += 1
print("The largest number is:", largest)
