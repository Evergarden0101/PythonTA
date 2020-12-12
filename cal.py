def cal_sum(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return -n + cal_sum(n - 1)
        else:
            return n + cal_sum(n - 1)


num = int(input())
print(cal_sum(num))
