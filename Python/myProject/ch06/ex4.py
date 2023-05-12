#ex4.py : 구구단

for i in range(2, 10, 1):
    print("# %d단 # " % i, end="")

for i in range(1, 10, 1):
    for j in range(2, 10, 1):
        print("%d X %d = %2d\t" %(i, j, i*j), end="")
    print("")