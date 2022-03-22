def MakeData(path):
    fhandle = open(path, "r")
    x=fhandle.readlines()
    y=[]
    for t in x:
        y.append(int(t))
    return y