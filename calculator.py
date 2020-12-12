t = int(input())
for i in range(t):
    a, b = map(float, input().split())
    op = input()
    if op == '+':
        print(round(a + b, 3))
    elif op == '-':
        print(round(a - b, 3))
    elif op == '*':
        print(round(a * b, 3))
    elif op == '/':
        print(round(a / b, 3))
