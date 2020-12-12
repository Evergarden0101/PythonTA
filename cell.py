cell = [1]
for i in range(1, 51):
    num = cell[i - 1] * 2
    if i >= 5:
        num -= cell[i - 5]
    cell.append(num)

t = int(input())
for i in range(t):
    n = int(input())
    print(cell[n])
