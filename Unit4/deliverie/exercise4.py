""" Exercise 4: Dynamic Programming - Patricia Cuesta Ruiz & Isabel Blanco Martínez """

values = [1, 3, 5, 9, 2]
weights = [1, 2, 3, 4, 5]


#Algorithm that calculates the maximum benefit from the two saddlebags
def maximum_benefit (values, weights, size, size2):
    aux = 0
    weight = 0
    lengthWeight = len(weights)
    total = 0
    total2 = 0
    saddlebag = []
    saddlebag2 = []
    saddlebag = create_saddlebag(lengthWeight+1, size+1, saddlebag)

    # We put the most expensive objects into the first saddlebag
    for i in range (len(values) + 1):
        for j in range (size + 1):
            # If the new object doesn't fit, we select the previous one
            if (weights[i-1] > j):
                saddlebag[i][j] = saddlebag[i-1][j]
            # If the object fits, decide if it is an optimal solution
            else:
                if (saddlebag[i-1][j] > (saddlebag[i-1][j-weights[i-1]] + values [i-1])):
                    saddlebag[i][j] = saddlebag[i-1][j]
                else:
                    saddlebag[i][j] = (saddlebag[i-1][j-weights[i-1]] + values[i-1])
            
            # The first saddlebag maximum benefit is obtained
            total = saddlebag[i][j]

    # We delete the objects selected by the first saddlebag in order to start with the second saddlebag
    while (aux <= lengthWeight):
        # We delete the object if the value is different than the previous one
        if ((lengthWeight - 1 - aux >= 0) and (saddlebag[lengthWeight - aux][size - weight] != saddlebag[lengthWeight-1 - aux][size - weight])):
            # We remove it from values and weights
            values.remove(values[lengthWeight - aux- 1])
            # We update the value of thw weitgh we are deleting
            weight = weight + weights[lengthWeight - aux- 1]
            weights.remove(weights[lengthWeight - aux- 1])
        
        aux += 1

    # The result of the previous loop is a brand new list for weights and values
    print ("Avaiable values for second saddlebag: ", values, " Avaiable weights for second saddlebag: ", weights)

    saddlebag2 = create_saddlebag(lengthWeight+1, size+1, saddlebag2)

    #We repeat the previous steps with the size of the second saddlebag
    for i in range (len(values) + 1):
        for j in range (size2 + 1):
            # If the new object doesn't fit, we select the previous one
            if (weights[i-1] > j):
                saddlebag2[i][j] = saddlebag2[i-1][j]
            # If the object fits, decide if it is an optimal solution
            else:
                if (saddlebag2[i-1][j] > (saddlebag2[i-1][j-weights[i-1]] + values [i-1])):
                    saddlebag2[i][j] = saddlebag2[i-1][j]
                else:
                    saddlebag2[i][j] = (saddlebag2[i-1][j-weights[i-1]] + values[i-1])
            
            # The first saddlebag maximum benefit is obtained
            total2 = saddlebag2[i][j]

    print ("First saddlebag: ")
    for i in range (len(saddlebag)):
        print(saddlebag[i], end="\n")

    print ("Second saddlebag: ")
    for i in range (len(saddlebag2)):
        print(saddlebag2[i], end="\n")

    return total + total2

def create_saddlebag (n, m, saddlebag):
    for i in range (n):
        elem = [0] * m
        saddlebag.append(elem)
    return saddlebag

# TESTER
print ("Avaiable values: ", values, " Avaiable weights: ", weights)
print("Total: ", maximum_benefit(values, weights, 6, 5))