def corking (bottles, stoppers, paired, first, index, pivot):
    if len(bottles) == 0:
        print("No bottles.")
    else:
        pivot = bottles[0]
        if first == True:
            for stopper in stoppers:
                if stopper < pivot:
                    table.insert(0, stopper)
                    print("The stopper", stopper, "has been added at the beginning of the table")
                    print("Table:", table)
                    index += 1
                elif stopper > pivot:
                    table.append(stopper)
                    print("The stopper", stopper, "has been added at the end of the table")
                    print("Table:", table)
                else: #if stopper == pivot then it gets paired
                    paired.append(bottles[0])
                    print("Bottle", bottles[0], "has been paired.")
                    print("Paired bottles:", paired)
        else:   
            for stopper in stoppers:
                if stopper == bottles[0]:
                    paired.append(bottles[0])
                    print("Bottle", bottles[0], "has been paired.")
                    print("Paired bottles:", paired)
        bottles.remove(bottles[0])
        if (len(bottles) != 0) and (pivot > bottles[0]):
            corking(bottles, table[0:index], paired, False, index, pivot)
        elif (len(bottles) != 0) and (pivot < bottles[0]):
            corking(bottles, table[index:len(table)], paired, False, index, pivot)


stoppers = [7, 12, 3, 1, 5, 10]
bottles = [5, 3, 10, 12, 1, 7]
table = []
paired = []

corking(bottles, stoppers, paired, True, 0, 0)