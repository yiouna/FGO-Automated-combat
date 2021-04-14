import random
import subprocess
import time

import cv2 as cv
import numpy as nu

import zhilin


def zhuzhan(img_2,img_role):
    """ img_1 传入的事实截图  img_2传入的需要对比的 ‘助战选择’ """
    zhilin.png()
    fgo_zhandou = cv.imread('images/zhandou.png')
    while True:
        res = cv.matchTemplate(fgo_zhandou, img_2, cv.TM_CCOEFF_NORMED)
        if (res >= 0.8).any():
            print('进入选择人物界面')
            zhuzhan_xuanzhe_jiaose(img_role)
            break
        else:
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            continue


def zhuzhan_xuanzhe_jiaose(img_role):
    """ img_rlle 传入的需要对比的细节图片 ‘校色名称’ """
    """ 职介坐标 """
    catser = [(838, 172), (869, 205)]  # 术士
    """ 选择坐标 """
    print('选择 catser')
    subprocess.run(f'adb shell input tap {random.randint(catser[0][0],catser[1][0])} {random.randint(catser[0][1],catser[1][1])}')
    time.sleep(random.uniform(0.5,1))
    zhilin.png()
    fgo_zhandou = cv.imread('images/zhandou.png')
    while True:
        res = cv.matchTemplate(fgo_zhandou, img_role, cv.TM_CCOEFF_NORMED)
        if (res >= 0.9).any():
            loc = nu.where(res >= 0.9)
            for i in zip(*loc[::-1]):
                subprocess.run(f'adb shell input tap {random.randint(i[0], i[0] + 500)} {random.randint(i[1], i[1] + 120)}')
                return
        else:
            print('没有检测到选择助战')
            print('移动屏幕')
            x_1 = random.randint(880, 1400)
            y_1 = random.randint(400, 450)
            subprocess.run(f'adb shell input swipe {x_1} {y_1} {x_1-100}  {y_1-320}')
            time.sleep(random.uniform(0.2,0.4))
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            continue


def start(fgo_startTask):
    """ fgo_startTask 开始任务图片 """
    zhilin.png()
    fgo_zhandou = cv.imread('images/zhandou.png')
    while True:
        print('开始对比')
        res = cv.matchTemplate(fgo_zhandou, fgo_startTask, cv.TM_CCOEFF_NORMED)
        if (res >= 0.85).any():
            loc = nu.where(res >= 0.85)
            for i in zip(*loc[::-1]):
                print(i)
                subprocess.run(f'adb shell input tap {random.randint(i[0],i[0]+150)} {random.randint(i[1],i[0]+40)}')
                break
            print('判断是否点击')
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            res = cv.matchTemplate(fgo_zhandou, fgo_startTask, cv.TM_CCOEFF_NORMED)
            if (res >= 0.85).any():
                print('没有点击成功')
                continue
            else:
                print('助战选择完毕')
                return
        else:
            print('未抓取到 开始任务，')
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            continue


