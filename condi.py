temp = float(input())
sch = input()

if temp >= 38:
    print('WARN')
else:
    if sch == 'BUAA':
        print('PASS')
    else:
        print('VISITOR')
