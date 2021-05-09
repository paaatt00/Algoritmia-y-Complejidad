def shrek(stairs):
    """
    OBJ: stairs must be welded from minimum to maximum, in order to find the 
    optimum solution.
    """
    stairs.sort()
    minimum = 0 
    for _ in range (len(stairs) - 1):
        j = stairs[0] + stairs[1]
        stairs.insert(binarySearch(j, stairs), j)
        minimum += j
        stairs = stairs[2:]
    return minimum

def binarySearch(num, stairs):
    if len(stairs) == 0: 
        ans = 0
    else:
        mid = len(stairs)//2
        if num < stairs[mid]: 
            ans = binarySearch(num, stairs[:mid])
        elif num > stairs[mid]:
            ans = binarySearch(num, stairs[mid + 1:]) + mid + 1
        else: 
            ans = mid
    return ans      
    
stairs = [10, 5, 7, 14, 2, 1, 3]
print("The minimum time Dragona needs to weld the stairs is", shrek(stairs))
