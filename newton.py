import matplotlib.pyplot as plt
import numpy as np

def get_func(msg):
    text = input(msg)
    def f(x):
        return eval(f"lambda x : {text}")(x)
    return f

def getNDDCoeffs(x, y):
    """ Creates NDD pyramid and extracts coeffs """
    n = np.shape(y)[0]
    pyramid = np.zeros([n, n]) 
    pyramid[::,0] = y 
    for j in range(1,n):
        for i in range(n-j):
            pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid

def main():
    f = get_func('Enter f(x) = ')
    xi = np.array(list(map(float, input("Enter xi:").split())))
    yi = np.array(list(map(f, xi)))
    ydd, *_ = getNDDCoeffs(xi, yi)
    n = len(xi)
    while True:
        ans = yi[0]
        try:
            x = float(input("Enter x: "))
        except:
            return
        for i in range(1,n):
            ans += ydd[i] * np.prod([(x - xi[k]) for k in range(i)])
            print(f"L{i}({x}) = {ans}")


if __name__ == '__main__':
    main()