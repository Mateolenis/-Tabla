#Fibonacci forma Recursiva

from re import X

def fib_r(n):
    if n < 2:
        return n 
    return fib_r(n-1) + fib_r(n-2)
for x in range(20):
    print(fib_r(x))

