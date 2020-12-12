t = int(input())
for i in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    ans = 1
    for j in range(n - 1):
        seq = False
        cnt = 1
        for k in range(j + 1, n):
            if seq:
                if w[k] > w[k - 1]:
                    cnt += 1
                    seq = not seq
                else:
                    break
            else:
                if w[k] < w[k - 1]:
                    cnt += 1
                    seq = not seq
                else:
                    break
        if cnt > ans:
            ans = cnt
    print(ans)
