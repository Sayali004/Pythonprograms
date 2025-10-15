i = int(input("Enter a number upto which you want to print numbers: "))
for num in range(1, i + 1):
    if num % 2 == 1:
        print(num, end=' ')
        
