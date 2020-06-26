 # 11-深度學習

---

## 簡介
深度學習為一種類神經網路，是一種以人工神經網路為架構，對資料進行表徵學習的演算法。常見的方法有三種:「卷積神經網路(CNN)、遞歸神經網路(RNN)、生成式對抗神經網路(GAN)」。

### 卷積神經網路
卷積神經網路是最常見的深度學習網路架構之一，因為網路架構中的卷積層(Convolutional layer)及池化層(Pooling layer)強化了模式辨識(Pattern recognition)及相鄰資料間的關係，使卷積神經網路應用在影像、聲音等訊號類型的資料型態能得到很好的效果。在著名程式AlphaGo中，也使用了變化過的卷積神經網路與蒙地卡羅樹搜尋演算法結合，得到驚人的棋力。

**卷積層**是卷積神經網路最核心的部份，通常由數十到數百個n x n的濾鏡(filter)組成，每個濾鏡會對不同的影像模式(Image pattern)進行強化，這些濾鏡實際強化的影像模式也是由訓練過程找出來的，所以卷積層可以針對不同的問題產生出不同的濾鏡效果。

**池化層**是類似訊號處理中的降維採樣(Down sampling)，通常會接在卷積層之後。一般用於影像識別的卷積神經網路，會在處理輸入資料時，有一到三次的卷積層加池化層的處理，之後再接兩層以上的完全連接層(Fully connected layer)，才輸出預測結果。

![](https://i.imgur.com/fZ4Vxje.png)


### 遞歸神經網路
遞歸神經網路(RNN)是近年來最蓬勃發展的深度學習網路架構，在架構上跟傳統的類神經網路有很大的不同。遞歸神經網路的神經元內有一個暫存的記憶空間，可以把先前輸入資料產生的狀態儲存在暫存的記憶空間(internal memory)內，之後神經元就可以根據之前的狀態而計算出不同的輸出值。因為遞歸神經網路可以儲存先前的狀態，所以可以處理不同長度的輸入資料，對時間序列(Time series)、自然語言處理(Nature language processing)、語音辨識等應用有非常好的效果。

雖然遞歸神經網路是如此強大，但在實務的訓練上卻有一些問題。權重組合的空間形狀對隨機梯度下降法很不利，有很平緩的地方也有非常陡峭的山谷。平緩的地方會有梯度消失(Vanishing gradient)的問題，會讓隨機梯度下降法停留在局部最佳解，而非常陡峭的山谷容易讓隨機梯度下降法更新後的數值跑出正常的範圍，使得隨機梯度下降法產生很不穩定的結果。

![](https://i.imgur.com/FTa5noh.png)


### 生成式對抗神經網路
生成式對抗神經網路(GAN)是非監督式學習的一種方法，通過讓兩個神經網路相互博弈的方式進行學習。

![](https://i.imgur.com/CIune5H.png)

##  參考資料
[課程資料](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/11-%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92) / [維基-深度學習](https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0) / [維基-GAN](https://zh.wikipedia.org/wiki/%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C) / [深度學習](https://research.sinica.edu.tw/deep-learning-2017-ai-month/) / [什麼是深度學習](https://speech.ee.ntu.edu.tw/~tlkagk/document/Basic.pdf) / [淺談神經網路原理及應用](http://www.cc.ntu.edu.tw/chinese/epaper/0038/20160920_3805.html)
