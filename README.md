# 用數學思維解決德州撲克牌型大小問題

甚麼叫做用數學來解決問題?
就是 用人請你實作平方和的時候
沒學過數學的人會寫這樣

```python
def sum_of_square(n):
    ans = 0
    for i in range(1, n+1):
        ans = ans + n**2
    return(ans)
```

但有學過的會直接帶公式 直接得出答案

```python
def sum_of_square(n):
    ans = (n) * (n+1) * (2*n + 1 ) / 6
    return( int(ans) )
```

讓電腦直接比 手牌 A 和 手牌 B 和 手牌 C 誰比較大
則實作起來較為麻煩
((想想 若為高牌，則要從最大張的牌一路比到最小張的牌。而且還有平手的可能…
若寫成 pesudo code 大概會變這樣

```python
H1 = [h1c1 h1c2 h1c3 h1c4 h1c5]
H2 = [h2c1 h2c2 h2c3 h2c4 h2c5]

# 第一大牌
if( h1c1 >  h2c1):
    return (H1)
if( h1c1 <  h2c1):
    return (H2)
if( h1c1 ==  h2c1):
    # 第2大牌比較
    if( h1c2 >  h2c2):
        return (H1)
    if( h1c2 <  h2c2):
        return (H2)
    if( h1c2 ==  h2c2):
        # 第3大牌比較
        if( h1c3 >  h2c3):
            return (H1)
        if( h1c3 <  h2c3):
            return (H2)
        if( h1c3 ==  h2c3):
                # 第4大牌比較
                ....
```

- **德州撲克規則**

以德州撲克來說，會先判斷牌型，再根據牌型決定比序標準
規則如下:
比序 1: 牌型 (同花順> 鐵支> 葫蘆> 同花> 順子> 三條 >兩對> 對子> 高牌)
比序 2~6 根據

| 牌型   | 比序 2   | 比序 3     | 比序 4     | 比序 5     | 比序 6 |
| ------ | -------- | ---------- | ---------- | ---------- | ------ |
| 高牌   | 最大牌   | 次大牌     | 第 3 大牌  | 次小牌     | 最小牌 |
| 對子   | 對子數字 | 單張最大牌 | 單張次大牌 | 單張最小牌 |
| 兩對   | 大對數字 | 小對數字   | 單張數字   |
| 三條   | 條子數字 | 單張大牌   | 單張小牌   |
| 順子   | 最大牌   |
| 同花   | 最大牌   | 次大牌     | 第 3 大牌  | 次小牌     | 最小牌 |
| 葫蘆   | 條子數字 | 對子數字   |
| 鐵支   | 鐵枝數字 | 單張數字   |
| 同花順 | 最大牌   |

若果要一個一個實做 會很累

不過 我們可以創造一個評分系統，幫手牌打分數
也就是是把手牌映射到一個 整數空間。
只要保證 若 手牌 A > 手牌 B 則 f(手牌 A) > f(手牌 B) 就可保證結果的正確性
(也就是 創造一個單調遞增函數)
電腦判斷哪副手牌較大時，則可用分數來判斷即可

# 評分系統

那具體來說要怎麼做呢?
我會對每個比序進行計分 然後再做加權
以保證 若 手牌 X 比序 1 得分 > 手牌 Y 比序 1 得分 則 f(手牌 X) > f(手牌 Y)

比序 1 計分方式如下
| 牌型 | 同花順 | 鐵支 | 葫蘆 | 同花 | 順子 | 三條 | 兩對 | 對子 | 高牌 |
|--- |---|---|---|---|---|---|---|---|---|
| 得分 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

比序 2~6 計分方式如下
| 牌面大小 | A | K | Q | J | 10 | 9 | 8 | 7 | 6 |5 |4 |3 |2 |
|--- |---|---|---|---|---|---|---|---|---|---|---|---|---|
| 得分 | 14\* | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 |5 |4 |3 |2 |

- 若有 12345 的順子 則將 A 視為 1 分

```shell
f(牌型) = 比序1得分*10*10^10 + 比序2得分*10^8 + 比序3得分*10^6 + 比序4得分*10^4 +  比序5得分*10^2 + 比序6得分*10^0
```

# 計分例子

## [範例 1] **梅花 K 紅心 K 磚塊 7 梅花 2 黑桃 5**

| 比序 | 比序 1 | 比序 2 | 比序 3 | 比序 4 | 比序 5 | 比序 6 |
| ---- | ------ | ------ | ------ | ------ | ------ | ------ |
| 結果 | 對子   | K      | 7      | 2      | 5      | X      |
| 得分 | 2      | 13     | 7      | 2      | 5      | 0      |

- **總得分**

```shell
f(梅花K 紅心K 磚塊7 梅花2 黑桃5)
= 2*10*10^10 + 13*10^8 + 7*10^6 + 2*10^4 +  5*10^2 + 0*10^0
= 21307020500
```

## [範例 2] **磚塊 A 磚塊 K 磚塊 Q 磚塊 10 磚塊 8**

| 比序 | 比序 1 | 比序 2 | 比序 3 | 比序 4 | 比序 5 | 比序 6 |
| ---- | ------ | ------ | ------ | ------ | ------ | ------ |
| 結果 | 同花   | A      | K      | Q      | 10     | 8      |
| 得分 | 6      | 14     | 13     | 12     | 10     | 8      |

- **總得分**

```shell
f(磚塊A 磚塊K 磚塊Q 磚塊10 磚塊8)
= 6*10*10^10 + 14*10^8 + 13*10^6 + 12*10^4 +  10*10^2 + 8*10^0
= 61413121008
```

## [範例 3] **黑桃 3 磚塊 4 梅花 5 磚塊 6 磚塊 7**

| 比序 | 比序 1 | 比序 2 | 比序 3 | 比序 4 | 比序 5 | 比序 6 |
| ---- | ------ | ------ | ------ | ------ | ------ | ------ |
| 結果 | 順子   | 7      | X      | X      | X      | X      |
| 得分 | 5      | 7      | 0      | 0      | 0      | 0      |

- **總得分**

```shell
f(黑桃3 磚塊4 梅花5 磚塊6 磚塊7)
= 5*10*10^10 + 7*10^8 + 0*10^6 + 0*10^4 +  0*10^2 + 0*10^0
= 50700000000
```
