'''
123456789
123456789
123456789
123456789
123456789
'''

n = int(input("Enter no of rows:"))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end= "")
    print()



n = int(input("enter number of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(64+j), end="")
    print()



