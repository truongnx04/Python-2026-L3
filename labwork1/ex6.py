#Using range(), create and print out the following sequence:
#range1: 0, 1, 2, 3, 4, 5, 6
#range2: 1, 4, 7, 10
#range3: 5, 4, 3, 2, 1
#range4: 6, 4, 2, 0, -2

range1 = range(0, 7)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)

print("range1:", *range1)
print("range2:", *range2)
print("range3:", *range3)
print("range4:", *range4)