#      A     
#     ABA    
#    ABCBA   
#   ABCDCBA  
#  ABCDEDCBA 
# ABCDEFEDCBA


n = 6
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(2*i+1):
        reverse = (2*i+1) // 2
        if j > reverse:
           print(chr(64+(2*i+1)-j),end="")
        else:
           print(chr(65+j),end="")
    print()
