''' 1111111111
    2222222222
    3333333333
    4444444444
    5555555555
    6666666666
    7777777777
    8888888888
    9999999999
    10101010101010101010
'''
n = int(input("enter number of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):  #    print(str(i)*10)  insted of second loop we can use this also
        print(i, end="")
    print()



n = int(input("enter number of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(64+i), end="")
    print()



