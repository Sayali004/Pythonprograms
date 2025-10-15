class NegativeNumberError(Exception):
    pass
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError
    else:
        print("You entered: ",num)
except NegativeNumberError:
    print("Exception: You entered Negative number!")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("End of program!")
