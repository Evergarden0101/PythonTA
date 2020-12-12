a = range(16)
i = 3
while i in a:
    if i ** 2 in a:
        i += 1
    elif i * 2 in a:
        i *= 2
    else:
        i += 14
    print(i, end=' ')
