# f (n) =(1+ p5)n −(1−p5)n2 np5.
import math


def fib(n):
    x = (1 + math.sqrt(5)) / 2
    y = (1 - math.sqrt(5)) / 2
    return round((x**n - y**n) / math.sqrt(5))


for i in range(10):
    print(fib(i), end=" ")
