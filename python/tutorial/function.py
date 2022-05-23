# 函式 function
# 函式碰到return，就不會運行下面的程式

def hello(name,age):     # 宣告函式
    print("hello" + name + "你今年" + str(age) + "歲") 
# hello("小白",87)

def add(a , b):  # 相加函式
    # print(a+b)
    c = a+b
    # return 10 # 把add(5,78)變成10
    return c
# print(add(5,7))

def swap(a , b): # 兩個數字對調
    temp = a
    a = b
    b = temp
    return a ,b
# print(swap(8, 3)) # 結果 => (3,8)

def question(num1 , num2):
    print(num1 + num2)   # 印出 7
    return 10    # 如果沒有寫，預設是return None
value = question(3,4)
print(value)  # 印出 10
