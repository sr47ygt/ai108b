# 02-爬山演算法
---
## 簡介
  爬山演算法 (Hill Climbing) 是一種最簡單的優化算法，該方法就像模擬人類爬山時的行為而設計的，因此稱為爬山演算法。
  
### 使用方法
  其主要目的為找尋最高點，首先隨機選取幾個數字，以左右比較的方式來尋找最高點(若新的值比較大則代替現在的值；沒有則保持原樣)。
  此方法只能找出局部最佳解，若山峰超過一個將無法找出所有最高點。
![](https://i.imgur.com/XGa1uJB.png)

## 梯度下降法
  梯度下降法(gradient descent)是最佳化理論裡面的一個一階找最佳解的一種方法，主要是希望用梯度下降法找到函數的局部最小值，因為梯度的方向是走向局部最大的方向，所以在梯度下降法中是往梯度的反方向走。
  使用前須注意是否可以微分，公式如下:
 ![](https://i.imgur.com/PbXvbgO.png)
 
缺點:
1. 靠近局部極小值時速度減慢。
2. 直線搜索可能會產生一些問題。
3. 可能會「之字型」地下降。


## 參考資料
爬山演算法:[1](https://www.itread01.com/hkpllxf.html) / [2](https://andy850701.pixnet.net/blog/post/463288544-%E5%95%9F%E7%99%BC%E5%BC%8F%E6%BC%94%E7%AE%97%E6%B3%95-%E2%80%93-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95) / [3](http://programmermagazine.github.io/201405/htm/focus1.html)

梯度下降法:[1](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95/A-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95%E7%B0%A1%E4%BB%8B) / [2](https://medium.com/@chih.sheng.huang821/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E5%9F%BA%E7%A4%8E%E6%95%B8%E5%AD%B8-%E4%BA%8C-%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95-gradient-descent-406e1fd001f) / [3](https://zh.wikipedia.org/wiki/%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95) / [4](https://hackmd.io/@allen108108/ryQypiDK4?type=view)
