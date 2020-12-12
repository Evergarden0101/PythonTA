n = int(input())
m5 = 0
m10 = 0
i = 0
while i < n:
    a, b = map(int, input().split())
    if b == 5:
        m5 += 1
    elif b == 10:
        m10 += 1
    if a == 1:
        charge = b - 5
    elif a == 2:
        charge = b - 10
    while charge > 0:
        if m10 > 0 and charge >= 10:
            charge -= 10
            m10 -= 1
        elif m5 > 0:
            charge -= 5
            m5 -= 1
        else:
            break
    if charge > 0:
        print(False)
        break
    i += 1
if i == n:
    print(True)
