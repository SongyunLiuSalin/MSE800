def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci series:")

    while a <= n:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp

    print()


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def main():
    n = int(input("Please enter a number: "))

    fibonacci(n)

    print("Factorial:", factorial(n))


main()