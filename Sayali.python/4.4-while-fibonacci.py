i = int(input("Enter a number upto which you want to print Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series upto", i, "is:", end=' ')
while a <= i:
    print(a, end=' ')
    a, b = b, a + b