def sum_calculate(aa, bb):
    r = 0
    for i in range(aa, bb + 1):
        print(i)
        r += i
    return r


# input a value in n

a = int(input("Enter A "))
b = int(input("Enter B "))
print("The Sum of", a, b, "is", sum_calculate(a, b))
