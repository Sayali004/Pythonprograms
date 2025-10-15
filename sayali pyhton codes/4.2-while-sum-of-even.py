n= int(input("Enter a number upto which you want to print sum of even numbers: "))
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print("The sum of even numbers upto", n, "is:", sum)