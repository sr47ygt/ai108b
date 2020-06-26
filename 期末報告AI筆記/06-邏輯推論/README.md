
# 06-邏輯推論

---
## 簡介
  邏輯推理就像我們講話一樣須有前因後果，一般來講可分為三個部分「前提、結論和規則」。
  
  ### 舉例來說:
  ```
  前提:天黑了
  規則:天黑路燈會打開
  結論:路燈亮了
 ```
  一般來說程式需要嚴格的判斷方式，通常都以公理系統來作為判斷標準。
  公理系統其實就是數學的 CPU 指令集，而其中布林代數為數學當中最簡單的系統，因為布林代數的値只有兩種--「真與假」 (或者用 0 與 1 代表)。
  
  ## 前向推論
  在邏輯中，特別是數理邏輯中，推理規則（推論規則）是構造有效推論的方案。這些方案建立在一組叫做前提的公式和叫做結論的斷言之間的語法關係。這些語法關係用於推理過程中，新的真的斷言從其他已知的斷言得出。規則也適用於非形式邏輯和邏輯論證，但是形式化更加困難和有爭議。

按照規定，推理規則的應用純粹是語法過程。儘管如此它必須是有效的，或者更精確地說保持有效性。為了使保持有效性的要求有意義，某種形式的語義與推理規則有關和推理規則自身的斷言是必需的。

### 以下面程式來解說:
 ```
 import random as r

role =[]
n = ['阿貓','阿狗','我','小明']
f = ['炒販','便當','泡麵','炸雞','拉麵','水餃','三明治','漢堡']
d = ['多多綠','奶茶','紅茶','烏龍茶','清茶','柳橙汁','豆漿']
t = ['中午','晚上','宵夜','早餐']
da = ['今天','明天','後天']



def S():
    return  N() + DAY() + TIME() + '想吃' + Food() + '配' + DRINK()

def N():
    return r.choice(n)

def Food():
    return r.choice(f)

def DRINK():
    return r.choice(d)

def TIME():
    return r.choice(t)

def DAY():
    return r.choice(da)

print(S())
```
  
  句子結構為:人+日期+時間+食物+飲料
  以這個結構下去做推論，得出下面結果
  ```
PS D:\python\ai\python\07-nlp\cword2vec> python HW5.py
小明後天中午想吃拉麵配奶茶
PS D:\python\ai\python\07-nlp\cword2vec> python HW5.py
我明天晚上想吃三明治配豆漿
PS D:\python\ai\python\07-nlp\cword2vec> python HW5.py
小明明天晚上想吃漢堡配清茶
PS D:\python\ai\python\07-nlp\cword2vec> python HW5.py
阿狗後天早餐想吃三明治配紅茶
PS D:\python\ai\python\07-nlp\cword2vec> python HW5.py
阿貓明天早餐想吃漢堡配紅茶
```

## 參考資料
[邏輯推論](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96) / [維基-邏輯推理](https://zh.wikipedia.org/wiki/%E9%80%BB%E8%BE%91%E6%8E%A8%E7%90%86) / [維基-演譯推理](https://zh.wikipedia.org/wiki/%E6%BC%94%E7%BB%8E%E6%8E%A8%E7%90%86) / [維基-推理規則](https://zh.wikipedia.org/wiki/%E6%8E%A8%E7%90%86%E8%A7%84%E5%88%99)
