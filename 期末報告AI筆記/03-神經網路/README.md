# 03-神經網路

---
## 簡介
  生物學上的神經元研究，啟發了AI領域關於「類神經網路」(或稱人工神經網路) 的概念。神經系統由神經元構成，彼此間透過突觸以電流傳遞訊號。是否傳遞訊號、取決於神經細胞接收到的訊號量，當訊號量超過了某個閾值(Threshold)時，細胞體就會產生電流、通過突觸傳到其他神經元。

  為了模擬神經細胞行為，科學家設定每一個神經元都是一個「激發函數」，其實就是一個公式；當對神經元輸入一個輸入值（input）後，經過激發函數的運算、輸出輸出值（output），這個輸出值會再傳入下一個神經元，成為該神經元的輸出值。如此這般，從第一層的「特徵向量」作為輸入值，一層層傳下去、直到最後一層輸出預測結果。
  ##  反傳遞法
  反向傳遞的目的就是利用最後的目標函數來進行參數的更新，一般來說都是用誤差均方和當作目標函數。
  
##  參考資料
[淺談神經網路](https://www.stockfeel.com.tw/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E7%9A%84%E8%A1%B0%E9%A0%B9%E8%88%88%E7%9B%9B%EF%BC%9A%E5%BE%9E%E9%A1%9E%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF%E5%88%B0%E6%B7%BA%E5%B1%A4%E5%AD%B8%E7%BF%92/) / [類神經網路，如何將生物分類?](https://pansci.asia/archives/163315) / [圖解27種神經模型](https://buzzorange.com/techorange/2018/01/24/neural-networks-compare/) / [機器學習-神經網路](https://medium.com/@chih.sheng.huang821/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF-%E5%A4%9A%E5%B1%A4%E6%84%9F%E7%9F%A5%E6%A9%9F-multilayer-perceptron-mlp-%E5%90%AB%E8%A9%B3%E7%B4%B0%E6%8E%A8%E5%B0%8E-ee4f3d5d1b41) / [維基-反向傳播法](https://zh.wikipedia.org/wiki/%E5%8F%8D%E5%90%91%E4%BC%A0%E6%92%AD%E7%AE%97%E6%B3%95)
