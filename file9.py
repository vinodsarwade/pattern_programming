# '''
# 12345678910
# 123456789
# 12345678
# 1234567
# 123456
# 12345
# 1234
# 123
# 12
# 1
# '''

# n = int(input("enter no of rows: "))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(j, end="")
#     print()

# '''
# 10101010101010101010
# 999999999
# 88888888
# 7777777
# 666666
# 55555
# 4444
# 333
# 22
# 1
# '''
# n = int(input("enter no of rows: "))
# for i in range(1, n+1):
#     for j in range(1,n+2-i):
#         print(n+1-i, end="")
#     print()


# '''
# AAAAAAAAAA
# BBBBBBBBB
# CCCCCCCC
# DDDDDDD
# EEEEEE
# FFFFF
# GGGG
# HHH
# II
# J
# '''

# n = int(input("enter no of rows: "))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+i), end="")
#     print()


# '''
# ABCDEFGHIJ
# ABCDEFGHI
# ABCDEFGH
# ABCDEFG
# ABCDEF
# ABCDE
# ABCD
# ABC
# AB
# A
# '''
# n = int(input("enter no of rows: "))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+j), end="")
#     print()



'''
JJJJJJJJJJ
IIIIIIIII
HHHHHHHH
GGGGGGG
FFFFFF
EEEEE
DDDD
CCC
BB
A
'''

n = int(input("enter no of rows: "))
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(chr(64+n+1-i), end="")
    print()