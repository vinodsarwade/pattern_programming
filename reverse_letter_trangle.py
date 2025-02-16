# A B C D E F
# A B C D E 
# A B C D
# A B C
# A B
# A

n = 6
for i in range(n+1):
    for j in range(1,n-i+1):
        print(chr(64+j),"", end="")
    print()
