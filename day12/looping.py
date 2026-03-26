'''
n=int(input("enter the size: "))
for row in range(n):
    for col in range(n):
        print("*", end=' ')
    print()

n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if (row + col) % 2 == 0:
            print('0', end='')
        else:
            print('1', end='')
    print()



   01234
0  01010
1  10101
2  01010
3  10101
4  01010





n = int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()


  01234
0 *
1 **
2 ***
3 ****
4 *****




n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()




n = int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()


n = int(input("Enter the size: "))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()



n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 or col==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''


n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
