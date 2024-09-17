'''
    *
   ***
  *****
 *******
*********
'''

n = int(input("enter no of rows: "))
for i in range(1, n+1):
    print(" "*(n-i),"*"*(2*i-1))


''' 
    1
   222
  33333
 4444444
555555555

'''
n = int(input("enter no of rows: "))
for i in range(1, n+1):
    print(" "*(n-i),(str(i)*(i*2-1)))




n = int(input("enter no of rows: "))   #same pattern for ABCD
for i in range(1, n+1):
    print(" "*(n-i),(str(chr(64+i))*(i*2-1)))