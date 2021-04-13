import os
import random
import time

import cv2 as cv

from lib import zhandou

img = cv.imread('images/002.png')
# 技能图标
fgo_baojuchongneng = cv.imread('images/fgo-baojuchongneng.png')
fgo_baojuchongneng_up = cv.imread('images/fgo-baojuchongneng_tisheng.png')
fgo_fangyu_dowm = cv.imread('images/fgo-fangyu-down.png')
fgo_lvka_up = cv.imread('images/fgo-lvka-up.png')
# 系统图标
fgo_gongji = cv.imread('images/fgo-gongji.png')
fgo_red = cv.imread('images/fgo-hong.png')
fgo_green = cv.imread('images/fgo-lv.png')
fgo_blue = cv.imread('images/fgo-lan.png')
fgo_opt = cv.imread('images/fgo-opt.png')
fgo_master_skill = cv.imread('images/fgo-master-skill.png')
"""  """
""" 第一回合 """
# round_1 = [[fgo_baojuchongneng, 1, True], ]
round_1 = {'role_1': [[fgo_baojuchongneng], True],
           'role_2': [],
           'role_3': [],
           'master': [], }
""" 第二回合 """
round_2 = {'role_1': [[fgo_lvka_up, fgo_fangyu_dowm], False, 'role_2'],
           'role_2': [[fgo_baojuchongneng_up], True, None],
           'role_3': [[fgo_lvka_up], False, 'role_2'],
           'master': [[fgo_baojuchongneng], False, 'role_2']}

""" 第三回合 """
round_3 = [[fgo_baojuchongneng, 3, False],
           [fgo_fangyu_dowm, 3, False]]


# 第二轮

os.system('adb shell screencap /sdcard/02.png')
os.system('adb pull /sdcard/02.png images/zhandou.png')
fgo_zhandou = cv.imread('images/zhandou.png')
loc_master = None
if round_2['master'][0]:
    print('本轮有master技能')
    loc_master = zhandou.master_skill(fgo_zhandou,fgo_master_skill)
    os.system(f'adb shell input tap {random.randint(loc_master[0], loc_master[0] + 50)} {random.randint(loc_master[1], loc_master[1] + 50)}')
    os.system('adb shell screencap /sdcard/02.png')
    os.system('adb pull /sdcard/02.png images/zhandou.png')
    fgo_zhandou = cv.imread('images/zhandou.png')

""" 第二轮 """

role_id, huihe_2 = [], []
for i in round_2:
    if not round_2[i]:
        break
    if round_2[i][1]:
        role_id.append(i)
    for y in round_2[i][0]:
        pos = zhandou.skill(fgo_zhandou, y)
        loc = zhandou.role(pos, i, round_2[i][2])

        huihe_2.append(loc)
print('本轮释放宝具角色',role_id)
print(huihe_2)
# 使用技能
print('开始使用技能')
for i in huihe_2:
    if 1940 > i[0] >1550 and 630 > i[1] > 400:
        print('检测到技能为 matser 技能')
        os.system(f'adb shell input tap {random.randint(loc_master[0], loc_master[0] + 50)} {random.randint(loc_master[1], loc_master[1] + 50)}')
        time.sleep(0.5)
    os.system(f'adb shell input tap {random.randint(i[0], i[0] + 50)} {random.randint(i[1], i[1] + 50)}')
    # 如果有需要技能的选择队友的
    if i[2] != None:
        time.sleep(1)
        zhandou.Skill_object(fgo_opt, i[2])
    time.sleep(3.5)


col = zhandou.attack(fgo_zhandou, fgo_gongji)
print(col)

os.system(f'adb shell input tap {random.randint(col[0], col[0] + 50)} {random.randint(col[1], col[1] + 50)}')
time.sleep(1)
# 开始确定使用卡牌
# 第二轮截图
time.sleep(1)
os.system('adb shell screencap /sdcard/02.png')
os.system('adb pull /sdcard/02.png images/zhandou.png')
fgo_zhandou = cv.imread('images/zhandou.png')
print('确定使用色卡')
red, green, blue = zhandou.attack_choose(fgo_zhandou, fgo_red, fgo_green, fgo_blue)
card = zhandou.attact_color(red, green, blue, role_id)
for i in card:
    os.system(f'adb shell input tap {random.randint(i[0], i[0] + 50)} {random.randint(i[1], i[1] + 50)}')
    time.sleep(0.5)

print('第二轮结束')