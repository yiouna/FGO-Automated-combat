import cv2 as cv

""" 战斗回合技能设置 """

rounds = [    {'role_1': [['fgo_baojuchongneng'], True, None],
     'role_2': [[], False, None],
     'role_3': [[], False, None],
     'master': [[], False, None], },
    {'role_1': [['fgo_lvka_up', 'fgo_fangyu_dowm'], False, 'role_2'],
     'role_2': [['fgo_baojuchongneng_up'], True, None],
     'role_3': [[], False, None],
     'master': [['fgo_baojuchongneng'], False, 'role_2']},

    {'role_1': [['fgo_baojuchongneng'], None, 'role_2'],
     'role_2': [[], True, None],
     'role_3': [['fgo_baojishanghai_up', 'fgo_fangyu_up', 'fgo_gongjili_up'], None, 'role_2'],
     'master': [[], False, None], },

]

""" 选择助战角色 """
# 目前只支持 Catser阶级 斯卡哈 诸葛孔明
servant = 'fgo_servant_zhugekongmin'
rank = 'Catser'

""" 战斗次数 """
nums = 2
