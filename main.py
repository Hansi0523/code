# 辨識色碼電阻(圖片)(算是已經完成了)

import cv2
import numpy as np

times = 0   # 計算點擊的次數

ten_copy = 0
unit_copy = 0
ten_plus_unit = 0

def mouse_activite(event, x, y, flag, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        print("x座標:{}, y座標{}".format(x, y))

        B, G, R = cv2.split(image)
        b, g, r = B[y, x], G[y, x], R[y, x]
        print("r, g, b = {}, {}, {}".format(r, g, b))

        global times  # 這裡要設global，才能對times做改變
        times = times + 1
        print("你按了 {} 次".format(times))

        show(r, g, b)
        what_color(r, g, b)



def show(r, g, b):
    solo_color = np.array([[[b, g, r]]], np.uint8)  # 重要(不要忘記!)
    cv2.namedWindow("show_solo_color", cv2.WINDOW_NORMAL)
    cv2.imshow("show_solo_color", solo_color)

def what_color(r, g, b):   # 判斷是哪種顏色，這部份參數，沒有調很準
    if r > 180 and g < 80 and b < 100:           # 2
        calculate(2, 2, 2)
        print("紅色")
    elif r > 180 and 80 <= g < 160 and b < 100:  # 3
        calculate(3, 3, 3)
        print("橙色")
    elif r > 180 and 160 <= g <= 255 and b < 100:  # 4
        calculate(4, 4, 4)
        print("黃色")
    elif 0 <= r < 100 and g >= 170 and 0 <= b < 150:  # 5
        calculate(5, 5, 5)
        print("綠色")
    elif 0 <= r < 100 and g >= 0 and b >= 200:   # 6
        calculate(6, 6, 6)
        print("藍色")
    elif 150 <= r <= 255 and 0 <= g <= 115 and 200 <= b <= 255:  # 7
        calculate(7, 7, 7)
        print("紫色")
    elif r < -1:    # 我不判斷灰色，因為很少用(其實是我懶的判斷)   # 8
        print("灰色")
    elif r > 250 and g > 250 and b > 250:     # 9
        calculate(9, 9, 9)
        print("白色")
    elif 0 <= r <= 65 and 0 <= g <= 65 and 0 <= b <= 65:        # 0
        calculate(0, 0, 0)
        print("黑色")
    elif 120 <= r <= 210 and 0 <= g <= 105 and 0 <= b <= 70:    # 1
        calculate(1, 1, 1)
        print("棕色")

def calculate(unit, ten, pow):     # 此函式是計算電阻值
    global ten_copy       # 這裡要global才能做更改數值
    global unit_copy      #
    global ten_plus_unit  #

    if times == 1:   # 按第一次為十位數
        ten_copy = ten * 10
        print("十位數:{}".format(ten_copy))
    if times == 2:   # 按第二次為個位數
        unit_copy = unit * 1
        print("個位數:{}".format(unit_copy))
    if times == 3:   # 按第三次為10的幾次方，並且把電阻值印出來
        ten_plus_unit = ten_copy + unit_copy
        print("十位數加個位數 : {}".format(ten_plus_unit))
        print("10的 {} 次方".format(pow))

        print(str(ten_plus_unit * (10 ** pow) / 1000) + "k歐姆")


image = cv2.imread("resistor_0.22k.jpg")
image = cv2.resize(image, (0, 0), fx=0.8, fy=0.8)
cv2.imshow("title", image)
cv2.namedWindow("title")
cv2.setMouseCallback("title", mouse_activite)

# high, width = image.shape[0:2]   # 得寬600, 高600
# print("寬:{}, 高:{}".format(high, width))

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()

