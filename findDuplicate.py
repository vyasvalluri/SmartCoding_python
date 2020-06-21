import sys
import time

# 20k elements 12.68 sec
def findDuplicate1(ind):
    l = len(ind)
    for i in range(l):
        for j in range(i+1, l):
            if(ind[i] == ind[j]):
                return ind[i]
    return sys.minvalue

#for 20k elements 0.0027 sec
def findDuplicate2(ind):
    l = len(ind)
    ind.sort()
    for i in range(1, l):
        if(ind[i] == ind[i-1]):
            return ind[i]

    return sys.minvalue

def findDuplicate3(ind):
    l = len(ind)
    aux = [bool] * l
    for i in range(l):
        tmp = ind[i]
        if(aux[tmp] == True) :
            return tmp
        aux[tmp] = True
    return sys.minvalue

def findDuplicate4(ind):
    l = len(ind)
    for i in range(l):
        tmp = abs(ind[i])
        if(ind[tmp] < 0) :
            return tmp
        ind[tmp] *= -1
    return sys.minvalue


def testcase1(ind):
    n = len(ind)
    for i in range(n-1):
        ind[i] = i+1
    ind[n-1] = n-1
    
def main():
    n = int(sys.argv[1])
    ind = [int] * n
    testcase1(ind)
    start = time.time()
    print(findDuplicate2(ind))
    end = time.time()
    print("time : ", (end - start))

if __name__ == "__main__":
    main()

