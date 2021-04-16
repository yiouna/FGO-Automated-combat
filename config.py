import cv2 as cv

""" 战斗回合技能设置 """

rounds = [    {'role_1': [['fgo_baojuchongneng'], True, None],
     'role_2': [[], False, None],
     'role_3': [[], False, None],
     'master': [[], False, None], },

    {'role_1': [['fgo_lvka_up', 'fgo_fangyu_dowm'], False, 'role_2'],
     'role_2': [['fgo_baojuchongneng_up'], True, None],
     'role_3': [['fgo_lvka_up'], False, 'role_2'],
     'master': [['fgo_baojuchongneng'], False, 'role_2']},

    {'role_1': [['fgo_baojuchongneng'], None, 'role_2'],
     'role_2': [[], True, None],
     'role_3': [['fgo_baojuchongneng','fgo_fangyu_dowm'], None, 'role_2'],
     'master': [[], False, None], },

]

""" 选择助战角色 """
servant = 'fgo_servant_sikadi_sikaha'
""" 
fgo_servant_zhugekongmin 诸葛孔明       Catser阶级
fgo_servant_sikadi_sikaha 斯卡哈·斯卡蒂   Catser阶级
fgo_servant_meiling       梅林            Catser阶级
 
"""
rank = 'Catser'


""" 战斗次数 """
nums = 5
""" 体力不足补充 """
Apple = '银苹果'  # 不支持铜苹果 容易出问题

"""
圣晶石
金苹果
银苹果
"""