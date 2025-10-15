#program to print reverse of the given number using while loop
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print("Reverse of the number is:", rev)

