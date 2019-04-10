i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i += 1
    print("Numbers now ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)

print("-----------------------------")

def calculo(a):
    for c in a:
        print(c)

calculo([0, 2, 3, 6])