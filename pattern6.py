# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
i=0
num=int(input("enter number"))
while i<=num:
    j=0
    while j<num-i:
        print(num-i,end=" ")
        j=j+1
    print()
    i=i+1