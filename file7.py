'''
1
12
123
1234
12345
123456
1234567
12345678
123456789
'''

n = int(input("enter no of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()



'''
A
AB
ABC
ABCD
ABCDE
ABCDEF
ABCDEFG
ABCDEFG
ABCDEFGHI
ABCDEFGHIJ
'''

n = int(input("enter no of rows: "))   # for charactor
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64+j),end="")
    print()