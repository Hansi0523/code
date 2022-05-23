# 問答程式
from question import Question # 只會引入Question這個類別
# import question # 整個檔案都import進來

test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\nanswer:",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\nanswer:",
    "香蕉是什麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\nanswer:"
]

questions = [
    Question(test[0] , "c"),
    Question(test[1] , "b"),
    Question(test[2] , "b")
]

def run_test(x):
    score = 0
    for a in x:
        answer = input(a.description)
        print("")
        if answer == a.answer:
            score += 1
    # a = Question("1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n", "c") 以第一個為例
    #              "       description            ","answer"


    print("你得到" + str(score) + "分，共" + str(len(x)) + "題")        


run_test(questions)

# print(test[0])
# print(test[1])
# print(test[2])
