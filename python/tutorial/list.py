# 列表list、列表的用法

scores = [90, 80 , 70 , 60 ,50]  # list  記得要是中括號[]
friends = ["小黑" , "小黃" , "小綠"]
things = [90 , "小黑" , True]
# print(scores)
# print(friends)
# print(things)
# print(scores[0]) # 取得scores的 90 分
# print(scores[3]) # 取得scores的 60 分
# print(scores[-1]) # 取得scores的 50 分 。 -1 代表是到數第一位
# print(scores[-2]) # 取得scores的 60 分 。 -2 代表是到數第二位
# print(scores[0:2]) # 從第0位開始取到第2位，不包含第2位，結果[90,80]
# print(scores[1:4]) # 從第2位開始取到第4位，不包含第4位，結果[80,70,60]
# print(scores[1:]) # 從第1位開始取到結束，結果[80,70,60,50]
# print(scores[:4]) # 取到第四位以前，但不包含第四位，結結果[90,80,70,60]
# scores[0] = 30  # 把scores[0]的分數改成30，原本是 90 -> 30

# scores.extend(friends)  # extend 擴增，也就是在scores列表中，再加一個friends的列表
# scores.append(40)   # append 在後面會多加一個值。結果[90, 80 , 70 , 60 , 50 ,40]
# scores.insert(2 , 30)  # 在第二位插入30。結果[90, 80 , 30 , 70 , 60 , 50]
# scores.remove(90) # 幫我把90給刪掉(移除掉)。結果[80, 70, 60, 50]
# scores.clear() # 把列表的東西全部刪掉。結果[]
# scores.pop() # pop 移除列表的最後一位。結果[90, 80, 70, 60]
# scores.sort() # sort 由小到大做排列。結果[50, 60, 70, 80, 90]
# scores.reverse() # reverse 反轉。[50, 60, 70, 80, 90] (50跟90對調，60跟80對調)

# print(scores.index(90)) # 回傳90在第幾個位置。結果 => 0
# print(scores.index(60)) # 回傳60在第幾個位置。結果 => 3  
# 備註 : 如果有兩個相同的數字，則會傳送最前面index值

# print(len(scores)) 取得scores的長度。結果 => 5
print(scores.count(60)) # 列表中有幾個60。結果 => 1
print(scores.count(20)) # 列表中有幾個20。結果 => 0

#-----------------------------------------
# phrase = "Hello Mr.White"
#         # 0123456789
# print(phrase[5])  # 印出 空白字元
# print(phrase[0:5]) # 從第0位開始取到第5位，但不包含第5位。結果 => Hello
# print(phrase[6:])  # 從第六位開始，取到結束。 結果 => Mr.White
#-----------------------------------------

# ---這樣做很麻煩---
# score1 = 90
# score2 = 80
# score3 = 70
# score4 = 60
# score5 = 50
# ------------------
