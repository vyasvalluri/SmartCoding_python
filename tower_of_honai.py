import sys
import time
def honai(n, src, aux, target):
    if(n == 1):
        print(src + "->"+target)
        return
    honai(n-1, src, target, aux)
    print(src+ "->"+target)
    honai(n-1, aux, src, target)


def main():
    n = int(sys.argv[1])
    start = time.time()
    honai(n, "A", "B", "C")
    end = time.time()
    print("time taken ", (end-start) )
    triange(n)

def triange(n):
    rows = n + 1
    for i in range(0, rows + 1, 1):
        for j in range(i + 1, rows + 1, 1):
            print(end=' ')
        for k in range(0, i, 1):
            print('*', end=' ')
        
        print('\n')
        

if __name__ == "__main__":
    main()