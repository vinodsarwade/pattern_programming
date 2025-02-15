#  *
#  **
#  *** 
#  ****
#  ***** 
#  ****
#  ***
#  **    
#  *

n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(1, n):
#     for j in range(0, n-i):
#         print("*", end="")
#     print()


for i in range(1, 2*n+1):
    stars = i
    if i > n:
        stars = 2*n-i
    for j in range(1, stars+1):     #initially print *  as i increases up to i > n  , 
        print("*", end="")          #once i > n then if condition satisfies and loop will start from (2*n- i)i.e: 2*5-6 = 4 then 2*5-7 = 3
    print()
