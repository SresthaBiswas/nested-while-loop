# *****
# ****
# ***
# **
# *
i=1
num=int(input("enter number"))
while i<=num:
    j=1
    while j<=num-i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1