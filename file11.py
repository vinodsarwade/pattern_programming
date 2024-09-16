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

n = int(input("enter no of rows: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


n = int(input("enter no of rows: "))   #for 1 extra space at start
for i in range(1, n+1):
    print(" "*(n-i),"*"*i,end="")
    print()

    