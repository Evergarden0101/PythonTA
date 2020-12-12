def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


t = int(input())
for i in range(t):
    n = int(input())
    j = 1
    while True:
        tmp = fibo(j)
        if tmp <= n:
            print(tmp, end=' ')
        else:
            print('')
            break
        j += 1
