'''
    1
   123
  12345
 1234567
123456789
'''

n = int(input("enter rows: "))
for i in range(1, n+1):
    print(" "*(n-i),end="")
    for j in range(1, i*2):
        print(j,end="")
    print()
