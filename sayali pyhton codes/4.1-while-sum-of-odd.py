n = int(input("Enter a number upto which you want to print sum of odd numbers: "))
i = 1
sum = 0
while i <= n:
    if i % 2 != 0:
        sum += i
    i += 1
print("The sum of odd numbers upto", n, "is:", sum)
