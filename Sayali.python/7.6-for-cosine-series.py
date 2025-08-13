n = int(input("Enter the value of n: "))
x = float(input("Enter the value of x (in radians): "))
cosine = 0
for i in range(n + 1):
    fact = 1
    for j in range(1, 2 * i + 1):
        fact *= j
    if i % 2 == 0:
        cosine += (x ** (2 * i)) / fact
    else:
        cosine -= (x ** (2 * i)) / fact
print("The cosine of x is:", cosine)
