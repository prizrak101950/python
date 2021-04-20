import sys
print(sys.version)
sys.setrecursionlimit(1000000)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact_iter(n):
    res = 1
    for i in range(1, n+1):
        res = res * i  # res *= i
    return res


num = 5

print(fact_iter(num))

print(fact(num))


