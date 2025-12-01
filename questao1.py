import numpy as np


def gauss(a, b, n, x, tol, er):
    s = np.zeros(n)
    er = 0
    for i in range(n):
        s[i] = abs(a[i][1])
        for j in range(1, n):
            if abs(a[i][j]) > s[i]:
                s[i] = abs(a[i][j])
    eliminate(a, s, n, b, tol, er)
    if er != -1:
        substitute(a, n, b, x)


def pivot(a, b, s, n, k):
    p = k
    maior = abs(a[k][k] / s[k])
    for ii in range(k+1, n):
        dummy = abs(a[ii][k] / s[ii])
        if dummy > maior:
            maior = dummy
            p = ii
    if p != k:
        for jj in range(k, n):
            dummy = a[p][jj]
            a[p][jj] = a[k][jj]
            a[k][jj] = dummy
        dummy = b[p]
        b[p] = b[k]
        b[k] = dummy
        dummy = s[p]
        s[p] = s[k]
        s[k] = dummy

def eliminate(a, s, n, b, tol, er):
    for k in range(n-1):
        pivot(a, b, s, n, k)
        if abs(a[k][k] / s[k]) < tol:
            er = -1
            break
        for i in range(k+1, n):
            fator = a[i][k] / a[k][k]
            for j in range(k+1, n):
                a[i][j] -= fator * a[k][j]
            b[i] -= fator * b[k]
    if abs(a[k][k] / s[k]) < tol:
        er = -1

def substitute(a, n, b, x):
    x[n-1] = b[n-1] / a[n-1][n-1]
    for i in range(n-2, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += a[i][j] * x[j]
        x[i] = (b[i] - soma) / a[i][i]

##############################
#        - 3x_2  + 7x_3  = 2 #
#   x_1  + 2x_2  -  x_3  = 3 #
#  5x_1  - 2x_2          = 2 #
##############################

def main():
    n = 3
    a = np.array([
        [0.0, -3.0, 7.0],
        [1.0,  2.0, -1.0],
        [5.0, -2.0, 0.0]
    ], dtype = float)
    b = np.array([2.0, 3.0, 2.0], dtype = float)
    x = np.zeros(n)
    tol = 1e-12
    er = 0
    print("Matriz A coeficientes:\n", a)
    print("Matriz B resultados:\n", b)
    gauss(a, b, n, x, tol, er)
    print("\nSolução encontrada:")
    print("x =", x)

if __name__ == "__main__":
    main()
