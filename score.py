def fibonacci(n):
    a = 0
    b = 1
    res = []
    res.append(1)
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n-1):
            c = a + b
            a = b
            b = c
            res.append(b)
            
        return sum(res)
 
n = int(input())
print(fibonacci(n+1))