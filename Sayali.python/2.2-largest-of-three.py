a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("First number is largest")
elif b >= a and b >= c:
    print("Second number is largest")
elif c >= a and c >= b:
    print("Third number is largest")
else:
    print("All three numbers are equal")
