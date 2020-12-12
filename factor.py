n = int(input())
for i in range(n):
    num = int(input())
    k = 1
    count = 0

    while k <= num:
        if num % k == 0:
            count += 1
        k += 1

    print(count)
