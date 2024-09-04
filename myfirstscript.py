# problem #1
# What is mising in the while loop?
# use a breakpoint in line 6 to debug
x = 1
while x < 10:
    print(x)
    # Incriment the value
    x += 1 


# problem #2
# use a breakpoint in line 14 to debug
# Mylist does not include 5, gives you index out of range error
mylist = list(range(5))

# change to (1,5)
for x in range(1,5):
    print(f"Run No.:{mylist[x]}")

