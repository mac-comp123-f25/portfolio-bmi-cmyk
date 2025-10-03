def printPairs(n, m):
    for i in range(n):
        for j in range(m):
            print( "(", i, j, ")" )

print("Testing with printPairs(3, 5):")
printPairs(3, 5)