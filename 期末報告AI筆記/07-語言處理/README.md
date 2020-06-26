  # 07-語言處理

---

## 簡介
語言分為自然語言與人造語言，自然語言就是所謂的母語，為一般交談的語言。人造語言的種類很多，但大部分都是程式類的語言，像是高階語言 (像是 C、Ruby、Python)、組合語言 (像是 x86、ARM、CPU0 的組合語言)、還有高階語言在翻譯成組合語言之前通常會經過某種中介語言等等。

程式語言以「詞彙、語句、文章」層層疊起，以下面四種方法疊起:
1. 詞彙掃描 : 詞彙層次 
2. 語法剖析 : 語句層次
3. 語意解析 : 文章層次
4. 語言合成 : 回應階段，將《詞彙》組合成《語句》、再將《語句》組合成《文章》呈現


### 以下面程式來解說:
下段為詞彙掃描:
 ```
 import random as r

role =[]
n = ['阿貓','阿狗','我','小明']
f = ['炒販','便當','泡麵','炸雞','拉麵','水餃','三明治','漢堡']
d = ['多多綠','奶茶','紅茶','烏龍茶','清茶','柳橙汁','豆漿']
t = ['中午','晚上','宵夜','早餐']
da = ['今天','明天','後天']
```
下段為句子結構:人+日期+時間+食物+飲料
```
def S():
    return  N() + DAY() + TIME() + '想吃' + Food() + '配' + DRINK()

```
這邊為隨機選取一個詞彙

```
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
這邊為程式結果
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
[語言處理](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/07-%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86) / [維基](https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E8%AA%9E%E8%A8%80)
