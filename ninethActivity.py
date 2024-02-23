while True:
    number = int(input("Insert a number: "))
    for i in range(1, 11):
        print(number, "X", i, " = ", (number * i))

    answer = str(input("Keep discovering the multiplication table? "))
    if answer != 'yes':
        break
