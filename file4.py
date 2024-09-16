'''
999999999999
888888888888
777777777777
666666666666
555555555555
444444444444
333333333333
222222222222
111111111111
'''

n = int (input("enter no of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(n+1-i, end=" ")
    print()



n = int (input("enter no of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(64+n+1-i), end=" ")
    print()



 