""" 战斗回合技能设置 """
# 小达芬奇 C呆毛 C呆毛
rounds = [
    {
        'role_1': [{'fgo_huifu': "", 'fgo_baojuweili_up': ""}, 'true'],
        'role_2': [{'fgo_gongjili_up': "", 'fgo_baojuchongneng': "role_1", 'fgo_lanka_up': "role_1"}, 'false'],
        'role_3': [{'fgo_gongjili_up': "", 'fgo_baojuchongneng': "role_1", 'fgo_lanka_up': "role_1"}, 'false'],
        'master': [{'fgo_baojuchongneng': "role_1"}, 'false']
    },
    {
        'role_1': [[], 'true'],
        'role_2': [[], 'false'],
        'role_3': [[], 'false'],
        'master': [[], 'false'],
    },
    {
        'role_1': [[], 'true'],
        'role_2': [[], 'false'],
        'role_3': [[], 'false'],
        'master': [[], 'false'],
    },
]
""" 选择助战角色 """
servant = 'fgo_servant_Cdai'
""" 
fgo_servant_zhugekongmin 诸葛孔明       Catser阶级
fgo_servant_sikadi_sikaha 斯卡哈·斯卡蒂   Catser阶级
fgo_servant_meiling       梅林            Catser阶级
fgo_servant_Cdai           C呆 
"""
rank = 'Catser'

""" 选择助战礼装 """

lizhuan = 'fgo_lizhuang_yilishabai_xiao'

# 不选择礼装筛选 及 lizhuan = '' 即可


""" 体力不足补充 """
Apple = '金苹果'  # 不支持铜苹果 容易出问题

"""
圣晶石
金苹果
银苹果
"""
