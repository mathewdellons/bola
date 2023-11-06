def f4(n):
    if n == 1 or n ==2:
        return 1
    return f4(n-1) + f4(n-2)

print(f4(5))
         
