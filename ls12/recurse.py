def fact_func(n):
    if n == 1:
        return 1
    return fact_func(n-1) * n
print(fact_func(30))