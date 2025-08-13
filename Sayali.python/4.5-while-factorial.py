k = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1
while i <= k:
    factorial *= i
    i += 1
print("The factorial of", k, "is:", factorial)
