# 如何使用字串、字串的用法
# print("Hello \nMr.Write") 換行\n
# print("Hello\" Mr.Write")  如何把雙引號加進去


# 函式 function
phrase = "Hello Mr.Write"
# print(phrase.lower()) lower全部變小寫
# print(phrase.upper()) upper全部變大寫
# print(phrase.isupper()) 判斷全部字母是否全都大寫，回傳bool
# print(phrase.islower()) 判斷全部字母是否全都小寫，回傳bool
# print(phrase.lower().islower()) 先全部變小寫，在判斷字母是否全都小寫，所以結果會是True

# print(phrase[0]) 回傳H
# print(phrase[6]) 回傳M 
# print(phrase.index("l")) 會先回傳最前面的l，所以是2
print(phrase.replace("l" , "L")) # 把小寫的l，替換成大寫的L