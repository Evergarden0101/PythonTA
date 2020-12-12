def func(y, *args):
    print('When {} Print Pass:'.format(y), end=' ')
    for i in args:
        if i % y == 0:
            continue
            print('Pass', end=' ')
        print(i, end=' ')


func(3, 4, 5, 6)
