import os
import random
import subprocess
import time
from resource_zhuzhan import * # 此模块已经导入 cv 了
import numpy as nu

import zhilin


"""===== 技能使用 ===== """
""" 创建一个战斗技能识别坐标 """
""" 同时用于结尾 """


def master_skill(img_1, fgo_master_skill, num=0.9):
    """
     镶嵌于 end 函数 内部
     镶嵌于 loop 函数内部
      """
    res = cv.matchTemplate(img_1, fgo_master_skill, cv.TM_CCOEFF_NORMED)
    if (res >= num).any():
        loc = nu.where(res >= num)
        for i in zip(*loc[::-1]):
            return i
    else:
        i = (1,)
        return i


def skill(img_1, img_2, num=0.859):
    res = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)
    pos = []

    """ res 内部的图像数组进项对比。 大于0.9 可以继续 """

    if (res >= num).any():
        """ 使用 any() 函数输出布尔值 只要有一个符合的  """
        loc = nu.where(res >= num)
        for i in zip(*loc[::-1]):
            pos.append(i)
    return pos


def Skill_object(opt_id):
    """ 对技能确认选择   fgo_opt"""
    """
    代码废弃
    os.system('adb shell screencap /sdcard/02.png')
    os.system('adb pull /sdcard/02.png images/zhandou.png')
    fgo_zhandou = cv.imread('images/zhandou.png')
    res = cv.matchTemplate(fgo_zhandou, fgo_opt, cv.TM_CCOEFF_NORMED)
        if (res >= 0.8).any():
    """
    print('进入技能选择 英灵阶段')
    if opt_id == 'role_1':
        print('选择 英灵 1')
        os.system(f'adb shell input tap {random.randint(600, 730)} {random.randint(630, 730)}')
    elif opt_id == 'role_2':
        print('选择 英灵 2')
        os.system(f'adb shell input tap {random.randint(1050, 1150)} {random.randint(630, 730)}')
    elif opt_id == 'role_3':
        print('选择 英灵 3')
        os.system(f'adb shell input tap {random.randint(1500, 1600)} {random.randint(630, 730)}')


# print(skill(img,img1))
def role(pos, role_id, ):
    """ 角色 1 2 3 进项筛选返回坐标 """
    if role_id == 'role_1':
        loc = pre(700, 250, 930, 800, pos, )
        return loc
    elif role_id == 'role_2':
        loc = pre(1160, 770, 930, 800, pos, )
        return loc
    elif role_id == 'role_3':
        loc = pre(1640, 1200, 930, 800, pos, )
        return loc
    elif role_id == 'master':
        loc = pre(1940, 1550, 630, 400, pos, )
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
    # 点开攻击
    res = cv.matchTemplate(img_1, img_2, cv.TM_CCOEFF_NORMED)
    attack_contrast = 0.7
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
    # lst = [('红卡', img_1, red), ('绿卡', img_2, green), ('蓝卡', img_3, blue)]
    lst_dict = {'红卡': [img_1, red], '绿卡': [img_2, green], '蓝卡': [img_3, blue]}
    for i in lst_dict:
        res = cv.matchTemplate(img_zhandou, lst_dict[i][0], cv.TM_CCOEFF_NORMED)
        contrast = 0.8
        if (res >= contrast).any():
            loc = nu.where(res >= contrast)
            for Ran in ran:
                for y in zip(*loc[::-1]):
                    if Ran[1] > y[0] > Ran[0] and 927 > y[1] > 757:
                        lst_dict[i][1].append(y)
                        break
    return red, green, blue


def attact_color(red, green, blue, role_id):
    """
    将attack_choose 返回的 结果 进行筛选
    目前是 优先选择红卡，其次绿卡，之后蓝卡
     """
    card = []
    for i in role_id:
        # 第一个角色宝具卡位置
        if i == 'role_1':
            x = (800, 300)
            card.append(x)
        elif i == 'role_2':
            x = (1150, 300)
            card.append(x)
        elif i == 'role_3':
            pass
    if len(card) == 3:
        return card

    if len(red) != 0:
        for i in red:
            i = i + ('红卡',)
            card.append(i)
            if len(card) == 3:
                return card
    if len(green) != 0:
        for i in green:
            i = i + ('绿卡',)
            card.append(i)
            if len(card) == 3:
                return card
    for i in blue:
        i = i + ('蓝卡',)
        card.append(i)
        if len(card) == 3:
            return card


def end(fgo_end_01, fgo_end_02, fgo_end_03, fgo_end_03_01, fgo_end_04, fgo_end_04_01, fgo_end_04_02, num_fix,):
    while True:
        zhilin.png()
        fgo_zhandou = cv.imread('images/zhandou.png')

        a = master_skill(fgo_zhandou, fgo_end_01, 0.8)
        b = master_skill(fgo_zhandou, fgo_end_02, 0.8)
        c = master_skill(fgo_zhandou, fgo_end_03, 0.8)
        d = master_skill(fgo_zhandou, fgo_end_04, 0.8)
        if len(a) == 2 or len(b) == 2:
            if len(a) == 2:
                print('从者羁绊')
                subprocess.run(
                    f'adb shell input tap {random.randint(a[0], a[0] + 250)} {random.randint(a[1], a[1] + 40)}')
                time.sleep(0.8)
            elif len(b) == 2:
                print('获得经验值')
                subprocess.run(
                    f'adb shell input tap {random.randint(b[0], b[0] + 250)} {random.randint(b[1], b[1] + 40)}')
                time.sleep(0.8)
        elif len(c) == 2 or len(d) == 2:
            if len(c) == 2:
                print('获得战利品')
                loc = master_skill(fgo_zhandou, fgo_end_03_01, 0.8)
                print('下一步')
                subprocess.run(
                    f'adb shell input tap {random.randint(loc[0], loc[0] + 160)} {random.randint(loc[1], loc[1] + 50)}')
                time.sleep(0.8)
            elif len(d) == 2:
                if num_fix:
                    loc = master_skill(fgo_zhandou, fgo_end_04_01, 0.8)  # 不继续
                    subprocess.run(
                        f'adb shell input tap {random.randint(loc[0] + 20, loc[0] + 160)} {random.randint(loc[1] + 5, loc[1] + 50)}')
                    print('结束脚本')
                    break
                else:
                    loc = master_skill(fgo_zhandou, fgo_end_04_02, 0.8)  # 继续
                    print('继续战斗')
                    subprocess.run(
                        f'adb shell input tap {random.randint(loc[0], loc[0] + 160)} {random.randint(loc[1], loc[1] + 50)}')
                    # 为了防止 截图间隔时间太短导致 连续点击 这边停顿一秒 再截图
                    time.sleep(1)
                    break
        else:
            time.sleep(random.uniform(0.5, 0.8))
            continue


def np(fgo_end_05, fgo_end_05_jin_Apple, fgo_end_05_yin_Apple, fgo_end_05_shenjinshi, fgo_end_05_ok, Apple):
    time.sleep(1.5)
    zhilin.png()
    fgo_zhandou = cv.imread('images/zhandou.png')
    loc = master_skill(fgo_zhandou, fgo_end_05)
    if len(loc) == 2:
        print('检测到体力不足')
        if Apple == '金苹果':
            loc = master_skill(fgo_zhandou, fgo_end_05_jin_Apple)
            subprocess.run(
                f'adb shell input tap {random.randint(loc[0], loc[0] + 100)} {random.randint(loc[1], loc[1] + 100)}')
        elif Apple == '银苹果':
            loc = master_skill(fgo_zhandou, fgo_end_05_yin_Apple)
            subprocess.run(
                f'adb shell input tap {random.randint(loc[0], loc[0] + 100)} {random.randint(loc[1], loc[1] + 100)}')

        elif Apple == '圣晶石':
            loc = master_skill(fgo_zhandou, fgo_end_05_shenjinshi)
            subprocess.run(
                f'adb shell input tap {random.randint(loc[0], loc[0] + 100)} {random.randint(loc[1], loc[1] + 100)}')
        while True:
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            loc = master_skill(fgo_zhandou, fgo_end_05_ok)
            if len(loc) == 2:
                subprocess.run(
                    f'adb shell input tap {random.randint(loc[0], loc[0] + 200)} {random.randint(loc[1], loc[1] + 50)}')
                print('体力补充完毕')
                break

    else:
        print('本次不需要补充体力')


""" 助战功能 """


def pol_zhuzhan_pandin_I(a):
    """
    助战 坐标筛选,所以阉割了 x轴内容
    """
    y_ = []
    for x, y in a:
        y_.append(y)

    temp_list = [y_[0]]
    temp = y_[0]
    for i in y_:
        if i - temp not in range(-20, 20):
            temp_list.append(i)
        temp = i

    return temp_list


def pol_zhuzhan_pandin_II(servant, lizhuan):
    """

    :param servant: servant y轴
    :param lizhuan: lzhuan  y轴
    :return:
    """
    for i in servant:
        for y in lizhuan:
            if y in range(i, i + 60):
                return i


def zhuzhan(img_2, servant, rank, lizhuan):
    """ servant传入的需要对比的 ‘助战选择’ rank 则是职介 """
    zhilin.png()
    fgo_zhandou = cv.imread('images/zhandou.png')
    while True:
        res = cv.matchTemplate(fgo_zhandou, img_2, cv.TM_CCOEFF_NORMED)
        if (res >= 0.8).any():
            print('进入选择人物界面')
            zhuzhan_xuanzhe_jiaose(servant, rank, lizhuan)
            break
        else:
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            continue


def zhuzhan_xuanzhe_jiaose(servant, rank, lizhuan):
    """ servant 传入的需要对比的细节图片 ‘校色名称’ """
    """ 职介坐标 """
    Catser = [(858, 154), (865, 200)]  # 术士
    """ 选择坐标 """
    if rank == 'Catser':
        subprocess.run(
            f'adb shell input tap {random.randint(Catser[0][0], Catser[1][0])} {random.randint(Catser[0][1], Catser[1][1])}')
        time.sleep(random.uniform(0.5, 1))
    zhilin.png()
    fgo_zhandou = cv.imread('images/zhandou.png')
    if len(lizhuan) == 0:
        num = 0
        while True:
            num += 1
            loc_servant = master_skill(fgo_zhandou, servant, )
            if len(loc_servant) == 2:
                subprocess.run(
                    f'adb shell input tap {random.randint(loc_servant[0], loc_servant[0] + 300)} {random.randint(loc_servant[1], loc_servant[1] + 120)}')
                print('选择完毕')
                return
            else:
                print('没有检测到选择助战')
                print('移动屏幕')
                x_1 = random.randint(880, 1400)
                y_1 = random.randint(400, 450)
                subprocess.run(f'adb shell input swipe {x_1} {y_1} {x_1 - 100}  {y_1 - 320}')
                time.sleep(random.uniform(0.2, 0.4))
                zhilin.png()
                fgo_zhandou = cv.imread('images/zhandou.png')
            if num >= 7:
                num = 0
                loc = master_skill(fgo_zhandou,fgo_zhuzhan_shuaxing)
                subprocess.run(f'adb shell input tap {random.randint(loc[0], loc[0] + 50)} {random.randint(loc[1], loc[1] + 40)}')
                time.sleep(random.uniform(0.2, 0.4))
                zhilin.png()
                fgo_zhandou = cv.imread('images/zhandou.png')
                loc = master_skill(fgo_zhandou, fgo_zhuzhan_shuaxing_OK)
                subprocess.run(f'adb shell input tap {random.randint(loc[0], loc[0] + 200)} {random.randint(loc[1], loc[1] + 50)}')
                print("刷新助战成功")



    else:
        num = 0
        while True:
            num += 1
            loc_servant = skill(fgo_zhandou, servant, )
            loc_lizhuan = skill(fgo_zhandou, lizhuan, )
            if loc_servant and loc_lizhuan:
                temp_y = pol_zhuzhan_pandin_II(pol_zhuzhan_pandin_I(loc_servant), pol_zhuzhan_pandin_I(loc_lizhuan))
                for i in loc_servant:
                    if temp_y in i:
                        subprocess.run(
                            f'adb shell input tap {random.randint(i[0], i[0] + 300)} {random.randint(i[1], i[1] + 120)}')
                        print('选择完毕')
                        return
            else:
                print('没有检测到选择合适助战/合适礼装')
                print('移动屏幕')
                x_1 = random.randint(880, 1400)
                y_1 = random.randint(400, 450)
                subprocess.run(f'adb shell input swipe {x_1} {y_1} {x_1 - 100}  {y_1 - 320}')
                time.sleep(random.uniform(0.2, 0.4))
                zhilin.png()
                fgo_zhandou = cv.imread('images/zhandou.png')

            if num >= 7:
                num = 0
                loc = master_skill(fgo_zhandou,fgo_zhuzhan_shuaxing)
                subprocess.run(f'adb shell input tap {random.randint(loc[0], loc[0] + 50)} {random.randint(loc[1], loc[1] + 40)}')
                time.sleep(random.uniform(0.2, 0.4))
                zhilin.png()
                fgo_zhandou = cv.imread('images/zhandou.png')
                loc = master_skill(fgo_zhandou, fgo_zhuzhan_shuaxing_OK)
                subprocess.run(f'adb shell input tap {random.randint(loc[0], loc[0] + 200)} {random.randint(loc[1], loc[1] + 50)}')
                print("刷新助战成功")