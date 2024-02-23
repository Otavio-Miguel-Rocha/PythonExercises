
number = int(input("Insert a number: "))
if number >= 0:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of ", number, " is ", factorial)
else:
    print("Wrong input")