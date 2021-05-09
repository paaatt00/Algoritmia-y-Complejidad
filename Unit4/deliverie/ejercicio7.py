""" Exercise 7: Dynamic Programming - Patricia Cuesta Ruiz & Isabel Blanco Martínez """

def sequence(a, b):
    sec = [] # to store the maximum subsequence
    m = [] # auxiliar table needed to obtain the subsequence
    m = createMatrix(len(a)+1, len(b)+1, m)

    # we use loops to fill the table comparing each bit from A among those from B.
    for i in range (len(a)):
        for j in range (len(b)):
            if (a[i] == b[j]): # if the bits are equal we obtain a bit
                # to the maximum subsequence and we keep all the bits
                # we might had before and keep comparing sequences
                m[i+1][j+1] = m[i][j] + 1

            elif (m[i][j] >= m[i+1][j]): # if bits are not equal
                # we cant increase the number of coincidences
                # and we must keep compating sequences
                m[i+1][j+1] = m[i][j+1]
                
            else:
                m[i+1][j+1] = m[i+1][j]

    # We print the matrix
    print("Matrix: ")
    for i in range (len(m)):
        print(m[i], end = "\n")
    print()

    i = 0 # Initialize rows of the matrix
    j = 0 # Initialize collums of the matrix
    k = 0 # Maximum length of the subsquence

    while (k < m[len(a)][len(b)]): # While k is minor to the last element
                    # of the matrix, we havent finished reading the matrix.
                    
        if (m[i+1][j+1] == m[i][j] + 1): #if a bit is equal in A and B
                    # we add it to the subsequence and increment K

            if (len(a) >= len(b)): # comparing A length to B length to
                    # decide which element we add to the subsequence
                sec.append(a[i])
            else:
                sec.append(b[j])
            k = k + 1

        # On the last row
        if (i < len(a)-1):
            i = i + 1

        if (j < len(b)-1):
            j = j + 1

    print("Subsequence: ", sec, end = 2 *"\n")
    return m[len(a)][len(b)]
        

def createMatrix(n, m, array):
    for i in range (n):
        elem = [0] * (m)
        array.append(elem)
        
    return array


# TESTER
a = [0, 1, 1]
#a = [0, 1, 1, 0]

b = [1, 0, 1, 0]
#b = [0, 0, 1, 1]
print("The subsequence length is: ", sequence(a, b))


