global a, b
a, b = 0, 1


def fib(n=None):    # write Fibonacci series up to n
    # global a, b
    global a, b
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)
print(a,b)

fib0 = fib(0)
print(fib0)