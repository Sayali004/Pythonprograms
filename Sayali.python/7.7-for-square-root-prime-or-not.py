import math
n = int(input("Enter a number to check if its square root is prime: "))
sqrt_n = math.isqrt(n)
for i in range(2, int(sqrt_n**0.5) + 1):
    if sqrt_n % i == 0:
        print(f"The square root of {n} is {sqrt_n}, which is not a prime number.")
        break
else:
    print(f"The square root of {n} is {sqrt_n}, which is a prime number.")