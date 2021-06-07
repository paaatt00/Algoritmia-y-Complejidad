def substitution(table, c1, c2):
    return table[index[c1]][index[c2]]

def algorithm(table, word, final):
    newChar = ""
    aux = ""
    listAux = []
    if (len(word) == 1):
        if (word == final):
            print("The objective has been reached: " + word)
            return True
        else:
            return False
    else:
        for i in range (len(word) - 1):
            newChar = substitution(table, word[i], word[i+1])
            aux = word.replace((word[i] + word[i+1]), newChar)
            if aux not in listAux:
                listAux.append(aux)
            aux = ""
        for j in range (len(listAux)):
            if (algorithm(table, listAux[j], final)):
                print("Path until the objective " + str(listAux[j]))
                return True
            else:
                algorithm(table, listAux[j], final)

table = [['b', 'b', 'a', 'd'],
         ['c', 'a', 'd', 'a'],
         ['b', 'a', 'c', 'c'],
         ['d', 'c', 'd', 'b']]
index = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
word = 'acabada'
final = 'd'
algorithm(table, word, final)