def factorial_calculate(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


# input a value in n

n = int(input("Enter "))
print("The factorial of", n, "is", factorial_calculate(n))
