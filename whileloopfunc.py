i = 0
numbers = []

def whilefunc(n):
    i = 0
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


whilefunc(3)



