n = int(input("Enter a number upto which you want to print sum: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("The sum of first", n, "natural numbers is:", sum)
