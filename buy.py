t = int(input())
for i in range(t):
    flg= False
    n, m = map(int, input().split())
    goods=[]
    stock=[]
    for j in range(n):
        name, num = map(str,input().split())
        goods.append(name)
        stock.append(int(num))
    for j in range(m):
        name = input()
        stock[goods.index(name)]-=1
        if stock[goods.index(name)] <0:
            flg=True
    if flg:
        print('Out of stock!')
    else:
        for j in range(n):
            print(stock[j])
    print()