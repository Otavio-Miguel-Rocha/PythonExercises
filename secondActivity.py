number = int(input("Insert a number smaller than 100: "))
if number > 100:
    print("The number must be smaller than 100")
else:
    print((number % 10) + (number % 10))
