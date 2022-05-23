# 二維列表、巢狀迴圈
# row 行
# column 列 (col)

# nums = [0,1,2,3,4]   # 一維列表

nums = [         # 二維列表(4行3列)
    [0,1,2],     # 上下數就是"行"
    [3,4,5],     # 左右數就是"列"
    [6,7,8],   
    [9]
]

#  行 列
#  [] []
# print(nums[0][2])  # 取到2
# print(nums[3][0])  # 取到9

for row in nums:  # 取到[0,1,2],[3,4,5],[6,7,8],[9]這四個列表，表示四行
    for col in row: # 假設第一行[0,1,2],再個別放入col這個變數裡面
        print(col)  # 印出列

