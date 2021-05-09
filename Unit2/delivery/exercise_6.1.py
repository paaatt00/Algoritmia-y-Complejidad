def shrek(stairs):
    """
    OBJ: stairs must be welded from minimum to maximum, in order to find the 
    optimum solution.
    """
    stairs.sort()
    minimum = 0 
    for _ in range (len(stairs) - 1):
        j = stairs[0] + stairs[1]
        minimum += j
        stairs = stairs[2:]
        stairs.append(j)
        stairs.sort()
    return minimum

stairs = [10, 5, 7, 14, 2, 1, 3] 
print("The minimum time Dragona needs to weld the stairs is", shrek(stairs))
