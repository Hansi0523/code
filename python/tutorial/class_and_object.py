# 類別class、物件object
class phone:    # class一個模板
    def __init__(self,os,number,is_waterproof):  # __init__ 初始的函式 self 物件的本身object
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
        
    # 物件函式 ----------------------  
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False

    def add(self,number1,number2):
        return number1+number2
    # 物件函式結束--------------------

phone1 = phone("ios",123,True)
# print(phone1.os)   # 結果 => iso
# print(phone1.number) # 結果 => 123
phone2 = phone("andriod",456,False)
# print(phone2.os) # 結果 => andriod

print(phone1.is_ios())  # 結果 => true

print(phone1.add(5,6))  # 結果 => 11