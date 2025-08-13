n = int(input("Enter the value of n: "))
sum = 0
for i in range(n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += 1 / fact
print("The sum of the sequence is:", sum)

