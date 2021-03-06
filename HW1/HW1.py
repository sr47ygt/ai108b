"""
A X = B ，求 X 是多少？

範例：題目來源: http://mail.im.tku.edu.tw/~idliaw/LinTup/99ie/99IEntu.pdf

5a+3b+6c=1
1a+1b+2c=2
2a+1b+3c=-1
"""
import gd1 as gd
import numpy as np

# A = np.array([[5.0,4,3],[2,2,1],4,3,1]])
# B = np.array([[3.0,1,-4]]).transpose()
A = np.array([[4.0,3,4],[5,5,7]])
B = np.array([[8.0, 10]]).transpose()

def f(p): #  能量函數:計算 ||AX-B||，也就是 ||Y-B||
    X = p
    Y = A.dot(X)
    # return np.linalg.norm(Y-B, 2)
    return np.linalg.norm(Y-B, 1)

# p = np.array([2.0, 2.0, 2.0])
p = np.array([0.0,0,0])
gd.gradientDescendent(f, p, step=0.01)
