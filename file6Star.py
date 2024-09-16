'''
*
**
***
****
*****
******
*******
********
*********
**********
'''

# n = int(input("enter no of rows: "))
# for i in range(1, n+1):
#     print("*"*i)

n = int(input("enter no of rows: "))   #for stars
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*",end="")
    print()



'''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''

n = int(input("enter no of rows: "))   # for numbers
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i,end="")
    print()



'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
JJJJJJJJJJ
'''

n = int(input("enter no of rows: "))   # for charactor
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64+i),end="")
    print()