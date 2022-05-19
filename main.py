import numpy as np
from newton import getNDDCoeffs

def main():
    o = int(input("Enter num of example: "))
    with open("data.txt", 'rt') as f:
        for _ in range(3 * (o - 1)):
            f.readline()
        f.readline()
        X = list(map(float, f.readline().split()))
        Y = list(map(float, f.readline().split()))
    ydd, *_ = getNDDCoeffs(X, Y)
    print("Coeff:\n", ydd)
    n = len(X)
    while True:
        ans = Y[0]
        try:
            x = float(input("Enter x: "))
        except:
            return
        for i in range(1,n):
            ans += ydd[i] * np.prod([(x - X[k]) for k in range(i)])
            print(f"L{i}({x}) = {ans}")

if __name__ == "__main__":
    main()