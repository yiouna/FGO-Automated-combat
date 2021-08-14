import random
import subprocess
import time
import zhilin

from config import *
from resource import *
from lib import zhuzhan, zhandou

import datetime


# adb devices 查看设备


def main(rounds, nums, servant, rank, Apple):
    """

    :param rounds: config 战后回合技能设定
    :param nums: 战斗次数
    :param servant: 助战从者
    :param rank: 助战从者 阶级
    :param Apple: 体力不足 使用苹果进行补充
    :return:
    """
    """ 进行战斗 """
    start = time.time()
    if servant == 'fgo_servant_zhugekongmin':
        print('本次战斗自动助战选择为诸葛孔明')
    elif servant == 'fgo_servant_sikadi_sikaha':
        print('本次战斗自动助战选择为斯卡哈·斯卡蒂')
    elif servant == 'fgo_servant_Cdai':
        print('本次战斗自动助战选择为C呆毛')

    for num in range(nums):
        print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]",
              f"开始进行第{num + 1}次战斗")
        for round_i in rounds:
            while True:
                zhilin.png()
                fgo_zhandou = cv.imread('images/zhandou.png')

                loc_master = zhandou.master_skill(fgo_zhandou, fgo_master_skill)
                if len(loc_master) == 1:
                    print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]",
                          '未到指定界面，等待')
                    time.sleep(1)
                    continue
                else:
                    print('本回合开始')
                    break
            if round_i['master'][0]:
                print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]",
                      '检测到本回合需要使用 master 技能')
                subprocess.run(
                    f'adb shell input tap {random.randint(loc_master[0], loc_master[0] + 50)} {random.randint(loc_master[1], loc_master[1] + 50)}')
                time.sleep(0.3)
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            role_id, huihe = [], []
            "对需要使用的技能进行坐标判断 ↓↓↓↓↓↓"
            for i in round_i:
                if round_i[i][1] == "true":
                    "是否使用宝具"
                    role_id.append(i)
                for y in round_i[i][0]:
                    pos = zhandou.skill(fgo_zhandou, globals()[y])
                    loc = zhandou.role(pos, i,)

                    huihe.append([loc, round_i[i][0][y]])
            print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]", '本轮释放宝具角色',
                  role_id)
            # 使用技能
            print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]",'开始使用技能')
            for i in huihe:
                if 1940 > i[0][0] > 1550 and 630 > i[0][1] > 400:
                    print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]",
                          '检测到技能为 matser 技能')
                    subprocess.run(
                        f'adb shell input tap {random.randint(loc_master[0], loc_master[0] + 50)} {random.randint(loc_master[1], loc_master[1] + 50)}')
                    time.sleep(0.4)
                subprocess.run(
                    f'adb shell input tap {random.randint(i[0][0], i[0][0] + 50)} {random.randint(i[0][1], i[0][1] + 50)}')
                # 如果有需要技能的选择队友的
                if i[1] != '':
                    time.sleep(0.5)
                    zhandou.Skill_object(i[1])
                time.sleep(3.4)

            col = zhandou.attack(fgo_zhandou, fgo_gongji)
            subprocess.run(
                f'adb shell input tap {random.randint(col[0], col[0] + 50)} {random.randint(col[1], col[1] + 50)}')
            time.sleep(1)
            # 开始确定使用卡牌
            time.sleep(1)
            zhilin.png()
            fgo_zhandou = cv.imread('images/zhandou.png')
            print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]", '确定使用色卡')
            red, green, blue = zhandou.attack_choose(fgo_zhandou, fgo_red, fgo_green, fgo_blue)
            card = zhandou.attact_color(red, green, blue, role_id)
            for i in card:
                subprocess.run(
                    f'adb shell input tap {random.randint(i[0], i[0] + 50)} {random.randint(i[1], i[1] + 50)}')
                time.sleep(0.4)
            print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]", '本回合结束')
        print("[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + f"[第{num + 1}回合]", '战斗结束，等待结算')
        if num + 1 == nums:
            num_fix = True
        else:
            num_fix = False
        zhandou.end(fgo_end_01, fgo_end_02, fgo_end_03, fgo_end_03_01, fgo_end_04, fgo_end_04_01, fgo_end_04_02,
                    num_fix, fgo_zhuzhan)
        if not num_fix:
            zhandou.np(fgo_end_05, fgo_end_05_jin_Apple, fgo_end_05_yin_Apple, fgo_end_05_shenjinshi, fgo_end_05_ok,
                       Apple)
            zhuzhan.zhuzhan(fgo_zhuzhan, globals()[servant], rank)

    end = time.time()
    print(f'一共用时{(end - start) / 60}分钟')


if __name__ == '__main__':
    # locals()  返回局部变量  globals() 返回全局变量
    xxxx = input("请将手机摆正充电口向右边.....任意键继续")
    nums = int(input("请输入战斗次数....:") or 20)
    main(rounds, nums, servant, rank, Apple)

