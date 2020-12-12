t = int(input())

for i in range(t):
    n = int(input())
    for j in range(2, n + 1):
        sum = 0
        for k in range(1, j):
            if j % k == 0:
                sum += k
        if sum == j:
            print(j, end=' ')
    print('')
