# 元組tuple
scores = (90 , 80 , 70 , 60 , 50) # 元組，是用小括號。複習:列表是用中括號
# print(scores[0])
# print(scores[0:2]) # 從第0位開始取，取到第二位，但不包含第二位。結果(90 , 80)
# print(len(scores)) # 取得長度。結果 => 5

# scores[0] = 30  # 元組跟列表的差別就是一旦創建了，元組裡面的資料就不行改變，也就是ReadOnly
# print(scores)   # 所以scores[0] = 30 是錯的，不能隨意修改資料

# 元組的功用是 => 防止資料被意外的修改
data = (123456 , 456789) # 例如我今天存放的是台北101的座標


