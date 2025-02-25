# F
# E F
# D E F
# C D E F
# B C D E F
# A B C D E F


n = 6 
for i in range(6, 0, -1):         #loop iterate from 6 -> 0  in reverse order -1
    for j in range(i, n+1):       # 1) i = 6 so  loop starts at 6-> 7 ie: F
                                  # 2) i = 5 so  loop starts at 5-> 7 ie: E F
        print(chr(64+j),end=" ")
    print()