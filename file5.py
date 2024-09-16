'''
987654321
987654321
987654321
987654321
987654321
987654321
'''

n = int (input("enter no of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(n+1-j, end=" ")
    print()



n = int (input("enter no of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(64+n+1-j), end=" ")
    print()
