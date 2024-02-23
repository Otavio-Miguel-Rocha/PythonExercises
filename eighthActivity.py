number = int(input("Insert a number: "))
print("Sequência de Fibonacci")
fb1 = 0
fb2 = 1

for i in range(2, number):
    fb = fb1 + fb2
    fb1 = fb2
    fb2 = fb
    print(fb)