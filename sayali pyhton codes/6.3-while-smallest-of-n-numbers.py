#smallest of n numbers using while loop
n = int(input("Enter the number of elements: "))
smallest = None
count = 0
while count < n:
    num = int(input("Enter a number: "))
    if smallest is None or num < smallest:
        smallest = num
    count += 1
print("The smallest number is:", smallest)
