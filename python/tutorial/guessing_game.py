# 猜數字遊戲(1~100)

# 我做的
# answer_number = 13
# while(1):
#     guess_number = int(input("請輸入一個數字: "))
#     if(guess_number > answer_number):
#         print("請在小一點")
#     elif(guess_number < answer_number):
#         print("大一點")
#     else:
#         print("恭喜你猜對了")
#         break
# print("遊戲結束")

# 網路上做的
# secret_num = 77
# guess = None
# while secret_num != guess:
#     guess = int(input("請輸入數字: "))
#     if guess > secret_num:
#         print("小一點")
#     elif guess < secret_num:
#         print("大一點")

# print("恭喜贏了")

# ----我是分隔線---------------------
# 只能被猜三次(多加的條件)

# 我自己做的
# answer_number = 13
# guess_times = 3 
# print("你只有三次的機會可以猜")
# while(1):
#     guess_number = int(input("請輸入一個數字: "))
#     if(guess_number > answer_number and guess_times > 0):
#         print("請在小一點")  
#         guess_times -= 1
#         print("你的猜測次數剩下 " + str(guess_times) + " 次")
#         print("")
#         if(guess_times == 0):
#             print("你的猜測次數沒了")
#             print("gg(༎ຶ⌑༎ຶ)")
#             break
#     elif(guess_number < answer_number and guess_times > 0):
#         print("大一點")
#         guess_times -= 1
#         print("你的猜測次數剩下 " + str(guess_times) + " 次")
#         print("")
#         if(guess_times == 0):
#             print("你的猜測次數沒了")
#             print("gg(༎ຶ⌑༎ຶ)")
#             break
#     else:
#         print("恭喜你猜對了")
#         print("well done!!!")
#         break
# print("迴圈結束")

# 網路上做的
secret_num = 77
guess = None
guess_count = 0
guess_limit = 3         # 我們最多能存放幾次
out_of_limit = False

while secret_num != guess and not(out_of_limit):   # 他沒有猜對 and 不能猜超過三次
    guess_count += 1       # 猜測的數字+1
    if guess_count <= guess_limit:  # 判斷"我們猜的次數"有沒有超過"猜的限制次數"
        guess = int(input("請輸入數字: "))
        if guess > secret_num:
            print("小一點")
        elif guess < secret_num:
            print("大一點")
    else:
        out_of_limit = True

if out_of_limit:       # out_of_limi == True
    print("抱歉 你輸了~")
else:                  # out_of_limi == False
    print("恭喜贏了")


