


def factFunt(f):
    factArr=[1]
    for i in range(f-1):
        factArr.append(factArr[i]*(i+2))
        print(factArr)
    return factArr


def suma(a,b):
    c=a+b
    print(c)
    return c
