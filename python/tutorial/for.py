# for 迴圈
# for 變數 in 字串OR列表:
#     要重複執行的程式碼

# for letter in "小白你好":
#     print(letter)     # 先印出小，在印出白，以此類推

# for num in [0,1,2,3,4]:  # 列表
#     print(num) # 先印出1，在印出2，以此類推

# for num in range(100):  # range(5) = [0,1,2,3,4]
#     print(num)

# for num in range(2,7):  # range(2,7) = [2,3,4,5,6]
#     print(num)

# 做次方函式
# print(pow(2 , 5))   # 2的5次方
# 2*2*2*2*2  乘了4次

# 我做的(看了網路寫的)
# def power(base , times):
#     original_number = 1
#     for nothing in range(times):
#         original_number = original_number * base 
#     return original_number    
# print(power(2 , 10))


# 網路做的(第一種寫法)
# 2  *2*2*2*2 (以2的5次方為例)
# def power(base_num , pow_num):
#     result = base_num    # 一開始已經有一個數字在那邊
#     for index in range(pow_num - 1):   # 所以這邊要減1
#         result = result * base_num 
#     return result


# 第二種寫法
# 1  *2*2*2*2*2*2 (以2的5次方為例)
def power(base_num , pow_num):
    result = 1   
    for index in range(pow_num):
        result = result * base_num
    return result

print(power(2 , 5))