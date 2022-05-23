# if 判斷句

# 1.
# 如果 我肚子餓
#     我就去吃飯
# hungry = True
# if hungry :
#     print("我就去吃飯")

# 2.
# 如果 今天下雨
#     我就開車去上班
# 否則
#     我就走路去上班
# rainy = False
# if rainy:
#     print("我就開車去上班") # rainy = True
# else:
#     print("我就走路去上班") # rainy = True

# 3.
# 如果 你考100分
#     我給你1000元
# 或是如果 你考80分以上
#     我給你500元
# 或是如果 你考60分以上
#     我給你100元
# 否則
#     你給我300元    
# score = input("請輸入成績 : ")
# new_score = int(score)
# if new_score > 100:
#     print("成績錯誤")
# elif new_score == 100:  # == 判斷左邊的值跟右邊的值有沒有相等
#     print(1000)
# elif new_score >= 80:
#     print(500)
# elif new_score >= 60:
#     print(100)
# elif 0 <= new_score < 60:
#     print(-300)
# else:
#     print("成績錯誤")

# 4.
# 如果 你考100分 且 今天下雨
#     我給你1000元
# 否則
#     你給我100元
# score = 90
# rainy = True
# if score == 100 and rainy:
#     print(1000)
# else:
#     print(-100)

# 5.
# 如果 你考100分 或 今天下雨
#     我給你1000元
# 否則
#     你給我100元
# score = 190
# rainy = False
# if score == 100 or rainy:
#     print(1000)
# else:
#     print(-100)

# 6.
# 如果 你考100分 或 沒有下雨
#     我給你1000元
# 否則
#     你給我100元
# score = 190
# rainy = True
# if score == 100 or not(rainy):
#     print(1000)
# else:
#     print(-100)

# 7.
# 如果 你沒有考100分 或 沒有下雨
#     我給你1000元
# 否則
#     你給我100元
# score = 190
# rainy = True
# if score != 100 or not(rainy):  # != => 不等於的意思
#     print(1000)
# else:
#     print(-100)

# 練習(我自己寫的)
def max_number(a , b  ,c):
    if a >= b and a >= c:
        max = a
    if b >= a and b >= c:
        max = b  
    if c >= a and c >= b:
        max = c  
    return max
# print(max_number(51 , 50 , 50))

# 練習(網路上寫的)
def max_num(num1 , num2  ,num3):
    if num1 >= num2 and num1 >= num3:
       return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(10 , 3 , 5))




