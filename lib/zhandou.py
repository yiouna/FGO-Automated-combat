import os, random
import numpy as nu
import cv2 as cv

img = cv.imread('../fgo-02.png')
img_chongenng = cv.imread('../fgo-chongeng.jpg')
img_gongji = cv.imread('../fgo-gongji.png')
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
        if 700 > x > 300 and 930 > y > 800:
            loc = (x, y)
            return loc

"""===== 指令牌 使用 ===== """

def attack(img_1, img_2):
    res = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)
    attack_contrast = 0.9
    if (res >= attack_contrast).any():
        loc = nu.where(res >= attack_contrast)
        for i in zip(*loc[::-1]):
            return i # 取第一个坐标即可

def attack_choose(img_1,img_2,img_3):
    """ 分别是 三张 红卡 绿卡 蓝卡"""
    pass



"""
pos = skill(img, img_chongenng)
loc = role(1, pos)
print(loc)
"""

A = attack(img,img_gongji)
print(A)