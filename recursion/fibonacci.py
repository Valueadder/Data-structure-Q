# program to implement fibonacci series with recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


n = int(input("Enter the number to find fibonacci:\n"))
print(fibonacci(n))
