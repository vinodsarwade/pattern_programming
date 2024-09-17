'''
*****
 ****
  ***
   **
    *
'''
n = int(input("enter rows: "))
for i in range(1, n+1):
    print(" "*(i-1),end="")
    for j in range(1, n+2-i):
        print("*",end="")
    print()


'''
55555
 4444
  333
   22
    1
'''
n = int(input("enter no of rows: "))
for i in range(1, n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(n+1-i, end="")
    print()

'''
ABCDE
 ABCD
  ABC
   AB
    A
'''

n = int(input("enter no of rows: "))
for i in range(1, n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(chr(64+j),end="")
    print() 