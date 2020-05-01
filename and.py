import gd2 as gd
import numpy as np
from numpy.linalg import norm
    
A = np.array([[0.0,0,1],
                [1,0,1],
                [0,1,1],
                [1,1,1]])

B = np.array([0.0,0,0,1]).transpose()

def f(p): #  能量函數:計算 ||AX-B||，也就是 ||Y-B||
    X = p
    Y = A.dot(X)
    return np.linalg.norm(Y-B, 1)

p = np.array([1.0,1,1])
p=gd.gradientDescendent(f, p, step=0.01)

print("\n==================================================================================\n")

print("p = {}".format(p))

print('w1={} w2={} b={} '.format(p[0], p[1], p[2]))

