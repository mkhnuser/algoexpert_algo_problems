def sameBsts(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    return arrayOne == arrayTwo


a1 = [5, 2, -1, 100, 45, 12, 8, -1, 8, 10, 15, 8, 12, 94, 81, 2, -34]
a2 = [5, 8, 10, 15, 2, 8, 12, 45, 100, 2, 12, 94, 81, -1, -1, -34, 8]
a1.sort()
a2.sort()
print(a1)
print(a2)
print(a1 == a2)
# NOTE: This does not work for some reason to solve this problem.
# Perhaps, lists as such are invalid BSTs.
