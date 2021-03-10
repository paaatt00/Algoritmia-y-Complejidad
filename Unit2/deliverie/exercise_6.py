def shrek(stairs):
    """
    OBJ: stairs must be welded from minimum to maximum, in order to find the 
    optimum solution.
    """
    stairs.sort()
    minimum = 0
    j = stairs[0]
    for i in range(1, len(stairs)):
        if (i == 1):
            j = j + stairs[1]
        else:
            j += stairs[i]
        minimum += j
    return minimum

stairs = [10, 5, 7, 14, 2, 1, 3]
print("The minimum time Dragona needs to weld the stairs is", shrek(stairs))

