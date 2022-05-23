# 模組module的使用
# pip 套件管理工具
import tool   # 我自己寫的模組
import token  # 也可以加入python內建的模組
import sys 
# import numpy  # 第三方的模組
import numpy as np # 把numpy改名成np

# print(tool.name)  # 印出tool裡面的name。結果 => 小白
# print(tool.age)  # 印出tool裡面的age。結果 => 87
# print(tool.max_num(2,3,88)) # 使用tool裡面的函式max_num。結果 => 88

print(sys.path)
