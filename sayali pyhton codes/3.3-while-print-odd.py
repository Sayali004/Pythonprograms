n = int(input("Enter a number upto which you want to print odd numbers: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1