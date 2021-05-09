class files(object):
    length = 0
    requests = 0
    def __init__(self, x, y):
        self.length = x
        self.requests = y

def initialize_tape(n):
    """ 
    OBJ: initialize the vector with n files and random values
    """
    from  random import randint
    files_list = []
    for _ in range(n):
        files_list.append(files(randint(1, 50), randint(1, 15)))
    return files_list

def order_tape(f):
    """
    OBJ: order the magnetic tape using bubble sort by dividing the length by the request number
    """
    for i in range(len(f)):
        for j in range(0, len(f)-i-1):
            if ((f[j].length / f[j].requests) > (f[j+1].length / f[j+1].requests)):
                f[j], f[j+1] = f[j+1], f[j]
    return f            

def test():
    files = order_tape(initialize_tape(20))
    for i in files:
        print("length: ", i.length, "request: ", i.requests, "l/r = ", i.length/i.requests)

test()