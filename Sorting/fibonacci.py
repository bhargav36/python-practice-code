## Fibonacci example 0 1 1 2 3 5 8 13 21 34 55
def fibo(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b
n = input("Enter sequence number:")

print(fibo(int(n)))