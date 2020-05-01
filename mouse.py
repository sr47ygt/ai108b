import numpy as np
def matrixPrint(m):
    for x in range(6):
        for y in range(8):
            if y == 7:
                print(m[x][y])
            else:
                print(m[x][y], end='')

def findPath(m,x,y):
    print("=========================")
    print("x=", x, " y=", y,)
    matrixPrint(m)
    if x>=6 or y>=8 :return False  #限制地圖大小
    if m[x][y] == '*' :return False  #地圖牆壁
    if m[x][y] == '+' :return False  #記住走過的點
    if m[x][y] == ' ' :m[x][y]='.'   #走的路徑
    if m[x][y] == '.'  and (x == 5  or  y==7) : #停止
        return True
    if y<7 and m[x][y+1]==' ' : 
        m[x][y]='.'
        if findPath(m, x,y+1) :return True #往右
    if x<5 and m[x+1][y]==' ' :
        m[x][y]='.'
        if findPath(m, x+1,y) :return True #往上
    if y>0 and m[x][y-1]==' ':
        m[x][y]=''
        if findPath(m, x,y-1) :return True #往左
    if x>0 and m[x-1][y]==' ' :
        m[x][y]='.'
        if findPath(m, x-1,y) :return True #往下
    m[x][y]=' '
    return False



map=(['*','*','*','*','*','*','*','*']
    ,[' ',' ','*','*','*','*','*','*']
    ,['*',' ',' ',' ',' ',' ',' ','*']
    ,['*','*','*','*',' ','*','*','*']
    ,['*','*',' ',' ',' ',' ','*','*']
    ,['*','*','*',' ','*','*','*','*'])
findPath(map, 1, 0)
print("=========================")
matrixPrint(map)