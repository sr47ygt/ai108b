## 程式
```
import cmath

def root2(a,b,c):
    t = b*b - 4*a*c
    t2 = cmath.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]

print("root of 8x^6+4x+2=", root2(8, 6, 4))
print("root of 7x^5+3x+1=", root2(7, 5, 3))
```
使用可以運算複數的函式庫(**cmath**)
## 結果
```
PS D:\python> & "C:/Program Files/Python37/python.exe" d:/python/python_class/ai/python/08-scientific/algebra/HW6.py
root of 8x^6+4x+2= [(-0.375+0.5994789404140899j), (-0.375-0.5994789404140899j)]
root of 7x^5+3x+1= [(-0.35714285714285715+0.5486532677049005j), (-0.35714285714285715-0.5486532677049005j)]
```
