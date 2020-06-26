# 05-電腦下棋

---
## 簡介
說道電腦下棋不能不提著名的AlphaGo，其是於2014年開始由英國倫敦Google DeepMind開發的人工智慧圍棋軟體，以及對應的電影紀錄片《AlphaGo世紀對決》。

專業術語上來說，AlphaGo的做法是使用了蒙地卡羅樹搜尋與兩個深度神經網路相結合的方法，其中一個是以估值網路來評估大量的選點，而以走棋網路來選擇落子。在這種設計下，電腦可以結合樹狀圖的長遠推斷，又可像人類的大腦一樣自發學習進行直覺訓練，以提高下棋實力。

以圍棋為例，需要有棋盤、規則、棋子(黑/白)，其他棋類也大同小異，只是規則改變。

## 蒙地卡羅樹搜尋
  蒙地卡羅樹搜尋，簡稱 MCTS，是在平均獲得利益的地方，採用模擬的結果，來給予平均利益。以圍棋進行 Monte-Carlo tree search 為例，選點時，會採用UCB回傳的值，做為選點的依據。當選點葉節點時，會展開一個新的節點。接著進行模擬，直到盤面結束，會給予勝負值。最後進行平均報酬率的更新。至此算是一個輪迴。Monte-Carlo tree search 進行多次的輪迴後，對於好點的節點深度會挖比較深，進而有利最後結束時，可以回傳一個好點。

### UCB
UCB(Upper Confidence Bound)是為了解決吃角子老虎問題所發展出來的公式。
![](https://i.imgur.com/z91Vq6G.png)
1. 平方根項：不確定性量測，估計a值的變異數
2. 分母：每次a被選擇，不確定性會變低因為Nt(a)在增加
3. 分子：natural logarithm伴隨時間推移，上界的增加量會變慢，但沒有上界
4. C：conﬁdence level

伴隨時間推移，所有的action最終都會被選擇，lower value被選擇的頻率也更低。

## 參考資料
[電腦下棋](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/05-%E9%9B%BB%E8%85%A6%E4%B8%8B%E6%A3%8B/A-%E9%9B%BB%E8%85%A6%E4%B8%8B%E6%A3%8B%E5%8F%B2) / [維基](https://zh.wikipedia.org/wiki/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%A0%91%E6%90%9C%E7%B4%A2) / [一個蒙地卡羅之電腦圍棋程式之設計](https://ir.nctu.edu.tw/bitstream/11536/45925/1/558001.pdf) / [蒙特卡羅搜尋](https://kknews.cc/zh-tw/news/z98yol.html) / [UCB](https://mc.ai/2-6-%E4%BF%A1%E8%B3%B4%E4%B8%8A%E7%95%8C%E5%8B%95%E4%BD%9C%E9%81%B8%E6%93%87upper-con%EF%AC%81dence-bound-action-selection/)

