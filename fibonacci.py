# Fibonacci-Zahlen

def print_fib(n):
    a, b = 0, 1     # Mehrfachzuweisung (multiple assignmet)
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fib_asLst(n):
    lst = list()
    a, b = 0, 1
    while b < n:
        lst.append(b)
        a, b = b, a + b
    return lst

print_fib(100)
print(fib_asLst(100))
