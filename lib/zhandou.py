import os, random
import numpy as nu
import cv2 as cv

img = cv.imread('../images/fgo-02.png')
img_chongenng = cv.imread('../images/fgo-chongeng.jpg')
img_gongji = cv.imread('../images/fgo-gongji.png')

img_zhandou = cv.imread('../images/fgo-zhandou.png')

img_hong = cv.imread('../images/fgo-hong.png')
img_lv = cv.imread('../images/fgo-lv.png')
img_lan = cv.imread('../images/fgo-lan.png')
"""===== 技能使用 ===== """
""" 创建一个战斗技能识别坐标 """


def skill(img_1, img_2):
    res = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)
    skill_contrast = 0.859
    pos = []

    """ res 内部的图像数组进项对比。 大于0.9 可以继续 """

    if (res >= skill_contrast).any():
        """ 使用 any() 函数输出布尔值 只要有一个符合的  """
        loc = nu.where(res >= skill_contrast)
        for i in zip(*loc[::-1]):
            pos.append(i)
    return pos


# print(skill(img,img1))
def role(role_id, pos):
    """ 角色 1 2 3 进项筛选返回坐标 """
    if role_id == 1:
        loc = pre(700, 300, 930, 800, pos)
        return loc
    elif role_id == 2:
        loc = pre(1160, 770, 930, 800, pos)
        return loc
    else:
        loc = pre(1640, 1250, 930, 800, pos)
        return loc


""" ==================== """


def pre(x_1, x_2, y_1, y_2, pos):
    """ 属于 role 内置判断函数 用于筛选坐标 """
    for i in pos:
        x = i[0]
        y = i[1]
        # if 700 > x > 300 and 930 > y > 800:
        if x_1 > x > x_2 and y_1 > y > y_2:
            loc = (x, y)
            return loc


"""===== 指令牌 使用 ===== """


def attack(img_1, img_2):
    res = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)
    attack_contrast = 0.9
    if (res >= attack_contrast).any():
        loc = nu.where(res >= attack_contrast)
        for i in zip(*loc[::-1]):
            return i  # 取第一个坐标即可


def attack_choose(img_zhandou, img_1, img_2, img_3):
    """
        分别是 三张 红卡 绿卡 蓝卡
        函数会自动分辨出五张卡牌的 x，y轴 进行返回
    """
    red = []
    green = []
    blue = []
    ran = [(295, 608, 1), (688, 973, 2), (1045, 1372, 3), (1148, 1769, 4), (1832, 2146, 5)]
    lst = [('红卡', img_1, red), ('绿卡', img_2, green), ('蓝卡', img_3, blue)]
    for i in lst:
        print(i[0])
        res = cv.matchTemplate(img_zhandou, i[1], cv.TM_CCOEFF_NORMED)
        contrast = 0.8
        if (res >= contrast).any():
            loc = nu.where(res >= contrast)
            for Ran in ran:
                for y in zip(*loc[::-1]):
                    if Ran[1] > y[0] > Ran[0] and 927 > y[1] > 757:
                        print(i[0], Ran[2])
                        i[2].append(y)
                        break
    return red, green, blue
"""
                for Ran in ran:
                    if Ran[1] > y[0] > Ran[0] and 927 > y[1] > 757:
                        print(i[0], Ran[2])
                        break
"""

"""
pos = skill(img, img_chongenng)
loc = role(1, pos)
print(loc)
"""

# A = attack(img,img_gongji)
# print(A)
'''
red, green, blue = attack_choose(img_zhandou, img_hong, img_lv, img_lan)
print(red, green, blue)
'''