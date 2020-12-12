def reverse(n):
    if n == 0:
        return
    else:
        unit = n % 10
        if unit != 0:
            print(unit, end='')
        return reverse(n // 10)


num = int(input())
reverse(num)
