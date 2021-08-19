""" 模式 模拟器/手机 """
# 目前只支持手机 mate30 充电口向左 mod = "mate30"
# 模拟器2340 * 1080 360 DIP     mod = "moniqi_1"
mod = "moniqi_1"

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
#lizhuan = ''

# 不选择礼装筛选 及 lizhuan = '' 即可


""" 体力不足补充 """
Apple = '金苹果'  # 不支持铜苹果 容易出问题

"""
圣晶石
金苹果
银苹果
"""


""" 一下内容 看不懂就别改 """

