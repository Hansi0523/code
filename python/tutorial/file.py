# 檔案的讀取、寫入
# open("檔案路徑" , mode = "開啟模式")


# 絕對路徑  ex : E:/python/school/python code/2/123.txt  
            # 斜線原本是 => \  要給它反過來 => /
# open("E:/python/school/python code/2/123.txt" , mode = "開啟模式")

# 相對路徑  以程式的位置做延伸 ex : 123.txt
            # 程式file.py的位子 : E:/python/school/python code/2
# open("2/123.txt" , mode = "開啟模式")


# mode = "r" 讀取read
# mode = "w" 複寫write
# mode = "a" 在原先的資料後寫東西

# --read模式-----------------------------------
# file = open("123.txt" , mode = "r")
# print(file.read())  # 全部讀取
# print(file.readline())  # readline() 只讀一行。

# for line in file: # 直接用for迴圈的方式讀取
#     print(line)

# print(file.readlines())  # 每一行的資料放到一個列表裡面

# file.close()   # 這樣才不會占用電腦的資源
# ---------------------------------------------

# --write模式--------------------------
# file = open("123.txt" , mode = "w")
# file.write("hi")
# file.close() 
#--------------------------------------

# --a模式--------------------------
file = open("123.txt" , mode = "a" , encoding="utf-8")  # encoding="utf-8" 支援中文
# file.write(" Mr.Write")
file.write("\n你好")
file.close() 
#--------------------------------------

# 用with的方式，可以省去file.close()的寫法
with open("123.txt" , mode = "a" , encoding="utf-8") as file: 
    file.write("\n哈哈")       


