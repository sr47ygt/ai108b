# 04-圖行搜索


---

## 簡介
  以離散數學與演算法來找出圖形中的目標節點，常用的方法有三種:「深度優先搜尋 (Depth-First Search, DFS)、廣度優先搜尋 (Breath-First Search, BFS)、最佳優先搜尋 (Best-First Search, BestFS)」。

### 深度優先搜尋(DFS)
  是一種用來遍尋一個樹(tree)或圖(graph)的演算法。由樹的根(或圖的某一點當成根)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目 的節點或遍尋全部節點。
  
![](https://i.imgur.com/i6NyUbM.png)
### 廣度優先搜尋法(BFS)
  是一種圖形(graph)搜索演算法。從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。
  
![](https://i.imgur.com/He5GMCq.png)

![](https://i.imgur.com/ldmBYWj.png)

## 參考資料
[深度優先搜尋法](http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html) / [深度與廣度優先搜尋法](https://magiclen.org/dfs-bfs/) / [維基-深度優先搜尋法](https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2) / [維基-廣度優先搜尋法](https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2) / [廣度優先搜尋法](http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html)
