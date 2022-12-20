# Code to create this shape
#
# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
# 2 2 2 2 2
# 2 2 2 2
# 2 2 2
# 2 2
# 2

depth = 6
for number in range(1, depth):
    for i in range(1, number + 1):
        print(1, end=' ')
    print("")
a=0
for i in range(depth-1, 0, -1):
    a += 1
    for j in range(1, i + 1):
        print(2, end=' ')
    print('\r')
