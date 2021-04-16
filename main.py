import random
import subprocess
import time
import zhilin

import cv2 as cv

from config import rounds, nums, servant, rank, Apple
from lib import zhuzhan, zhandou


# adb devices 查看设备


def main(rounds, nums, servant, rank , Apple):
    """ 技能图标 """
    # 宝具
    fgo_baojuchongneng = cv.imread('images/skill/fgo-baojuchongneng.png')
    fgo_baojuchongneng_up = cv.imread('images/skill/fgo-baojuchongneng_tisheng.png')
    # 暴击伤害
    fgo_baojishanghai_up = cv.imread('images/skill/fgo-baojishanghai-up.png')
    # 防御
    fgo_fangyu_up = cv.imread('images/skill/fgo-fangyu-up.png')
    fgo_fangyu_dowm = cv.imread('images/skill/fgo-fangyu-down.png')
    # 攻击力
    fgo_gongjili_up = cv.imread('images/skill/fgo-gongjili-up.png')
    # 色卡
    fgo_lvka_up = cv.imread('images/skill/fgo-lvka-up.png')
    fgo_hongka_up = cv.imread('images/skill/fgo-hongka-up.png')
    # 无敌
    fgo_wudi = cv.imread('images/skill/fgo-wudi.png')
    """ 游戏界面图标 """
    fgo_gongji = cv.imread('images/system/fgo-gongji.png')
    fgo_red = cv.imread('images/system/fgo-hong.png')
    fgo_green = cv.imread('images/system/fgo-lv.png')
    fgo_blue = cv.imread('images/system/fgo-lan.png')
    fgo_opt = cv.imread('images/system/fgo-opt.png')
    fgo_master_skill = cv.imread('images/system/fgo-master-skill.png')
    fgo_zhuzhan = cv.imread('images/system/fgo_zhuzhan.png')
    fgo_startTask = cv.imread('images/system/fgo_startTask.png')

    fgo_end_01 = cv.imread('images/system/fgo_end_01.png')
    fgo_end_02 = cv.imread('images/system/fgo_end_02.png')
    fgo_end_03 = cv.imread('images/system/fgo_end_03.png')
    fgo_end_03_01 = cv.imread('images/system/fgo_end_03_01.png')
    # 是否进行同一关卡
    fgo_end_04 = cv.imread('images/system/fgo_end_04.png')
    fgo_end_04_01 = cv.imread('images/system/fgo_end_04_01.png')
    fgo_end_04_02 = cv.imread('images/system/fgo_end_04_02.png')

    # 补充体力
    fgo_end_05 = cv.imread('images/system/fgo_end_05.png')
    fgo_end_05_shenjinshi = cv.imread('images/system/fgo_end_05_shenjinshi.png')
    fgo_end_05_jin_Apple = cv.imread('images/system/fgo_end_05_jin_Apple.png')
    fgo_end_05_yin_Apple =  cv.imread('images/system/fgo_end_05_yin_Apple.png')
    #fgo_end_05_tong_Apple =  cv.imread('images/system/fgo_end_05_tong_Apple.png')
    fgo_end_05_ok = cv.imread('images/system/fgo_end_05_ok.png')

    """ 助战角色 """
    fgo_servant_sikadi_sikaha = cv.imread('images/servant/fgo-servant-sikadi_sikaha.png')
    fgo_servant_zhugekongmin = cv.imread('images/servant/fgo-servant-zhugekongmin.png')
    fgo_servant_meiling = cv.imread('images/servant/fgo-servant-meiling.png')

    """ 开始战斗 """
    # zhuzhan.start(fgo_startTask)
    """ 进行战斗 """
    start = time.time()
    if servant == 'fgo_servant_zhugekongmin':
        print('本次战斗自动助战选择为诸葛孔明')
    elif servant == 'fgo_servant_sikadi_sikaha':
        print('本次战斗自动助战选择为斯卡哈·斯卡蒂')
    for num in range(nums):
        print(f"开始进行第{num + 1}次战斗")
        for round_i in rounds:
            while True:
                zhilin.png()
                fgo_zhandou = cv.imread('images/zhandou.png')

                loc_master = zhandou.master_skill(fgo_zhandou, fgo_master_skill)
                if len(loc_master) == 1:
                    print('未到指定界面，等待')
                    time.sleep(2)
                    continue
                else:
                    print('本回合开始')
                    break
            if round_i['master'][0]:
                print('检测到本回合需要使用 master 技能')
                subprocess.run(f'adb shell input tap {random.randint(loc_master[0], loc_master[0] + 50)} {random.randint(loc_master[1], loc_master[1] + 50)}')
                time.sleep(0.5)
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')

            role_id, huihe_2 = [], []
            for i in round_i:
                if not round_i[i]:
                    break
                if round_i[i][1]:
                    role_id.append(i)
                for y in round_i[i][0]:
                    pos = zhandou.skill(fgo_zhandou, locals()[y])
                    loc = zhandou.role(pos, i, round_i[i][2])

                    huihe_2.append(loc)
                    print(loc)
            print('本轮释放宝具角色', role_id)
            print(huihe_2)
            # 使用技能
            print('开始使用技能')
            for i in huihe_2:
                if 1940 > i[0] > 1550 and 630 > i[1] > 400:
                    print('检测到技能为 matser 技能')
                    subprocess.run(f'adb shell input tap {random.randint(loc_master[0], loc_master[0] + 50)} {random.randint(loc_master[1], loc_master[1] + 50)}')
                    time.sleep(0.5)
                subprocess.run(
                    f'adb shell input tap {random.randint(i[0], i[0] + 50)} {random.randint(i[1], i[1] + 50)}')
                # 如果有需要技能的选择队友的
                if i[2] != None:
                    time.sleep(1)
                    zhandou.Skill_object(fgo_opt, i[2])
                time.sleep(3.5)

            col = zhandou.attack(fgo_zhandou, fgo_gongji)
            print(col)

            subprocess.run(
                f'adb shell input tap {random.randint(col[0], col[0] + 50)} {random.randint(col[1], col[1] + 50)}')
            time.sleep(1)
            # 开始确定使用卡牌
            time.sleep(1)
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            print('确定使用色卡')
            red, green, blue = zhandou.attack_choose(fgo_zhandou, fgo_red, fgo_green, fgo_blue)
            card = zhandou.attact_color(red, green, blue, role_id)
            for i in card:
                subprocess.run(
                    f'adb shell input tap {random.randint(i[0], i[0] + 50)} {random.randint(i[1], i[1] + 50)}')
                time.sleep(0.5)
            print('本回合结束')
        print('战斗结束，等待结算')
        if num + 1 == nums:
            num_fix = True
        else:
            num_fix = False
        zhandou.end(fgo_end_01, fgo_end_02, fgo_end_03, fgo_end_03_01, fgo_end_04, fgo_end_04_01, fgo_end_04_02,
                    num_fix, fgo_zhuzhan)
        if not num_fix:
            zhandou.np(fgo_end_05, fgo_end_05_jin_Apple, fgo_end_05_yin_Apple, fgo_end_05_shenjinshi, fgo_end_05_ok, Apple)
            zhuzhan.zhuzhan(fgo_zhuzhan, locals()[servant], rank)

    end = time.time()
    print(f'一共用时{(end - start) / 60}分钟')


if __name__ == '__main__':
    main(rounds, nums, servant, rank, Apple)
