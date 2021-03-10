def minmax(vector):
    max = []
    min = []
    while (len(vector) > 1):
        if (vector[0] > vector[1]):
            max.append(vector[0])
            min.append(vector[1])
            del(vector[0])
            del(vector[0])
        else:
            max.append(vector[1])
            min.append(vector[0])
            del(vector[0]) 
            del(vector[0])
        if (len(vector) == 1):
            if (vector[0] > max[0]):
                max.append(vector[0])
                del(vector[0])
            else:
                min.append(vector[0])
                del(vector[0])
        maxM = max[0]
        for i in max:
            if (i > maxM):
                maxM = i
        minM = min[0]
        for i in min:
            if (i < minM):
                minM = i    
    print("The MIN value is", minM)
    print("The MAX value is", maxM)

vector = [2, 7, 15, 0, 200, 87, 151]
minmax(vector)
