try:
    num1=int(input("enter a number:"))
    num2=int(input("enter another number:"))
    result=num1/num2
    print("result is:",result)
except ZeroDivisionError:
    print("number cannot be divided by zero")
except ValueError:
    print("invalid input")
finally:
    print("End of program!")
