
for i in range(0,6):
    print('  '*(6-(i+1)),'* '*i)


n=65
for i in range(0,6):
    for j in range(i):
        print(chr(n),' ',end='')
        n = n + 1
    print('\n')
