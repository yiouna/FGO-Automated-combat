# Automated combat
一个  python 刷狗粮脚本。 使用opencv库<br>
## bilibili 视频 [点击](https://www.bilibili.com/video/av887505662)
## 前言 | 请一定看完!
啊啊啊啊 本脚本说是脚本 其实就是自定义战斗.优先级 宝具>红卡>绿卡>蓝卡 的运行逻辑.这个逻辑是不可改的,因为我并不是想写一个智能战斗脚本.
其实你自定义的 就是每个回合需要释放的技能,(包概御主技能).以及宝具的自动释放,
宝具的自动释放是根据人物顺序来得,如果同时释放宝具, 角色1 优先于 角色2 优先于 角色3 ,如果想调整位子就手动调整角色位置吧.
脚本运行流程如下:<br> 
(一开始的战斗需要手动进入)<br> 
>  检测是否进入战斗画面<br>  
  ↓
  第一回合<br>  
  ↓
  第二回合<br>  
  ↓  ...回合(看你自己设置了)<br>  
  ↓ ...结束<br>  
  ↓  体力不足   体力足够{无视下一步}<br>  
  ↓ 磕苹果(圣晶石 金苹果 银苹果都行 不过铜苹果不可以)<br> 
  ↓ 继续关卡<br> 
  ↓ 选择助战('自动选择设定的助战.自动选择设定的礼装,")<br> 
  ----如果没有现在到,在8个向下循环寻找后,会自动刷新列表重新查找<br> 
  ----目前并没有自动添加好友功能.下次更新则会添加.<br> 
  ↓ 下一个战斗循环
  
  #### 自言自语
  作为一个fgo的开服玩家,这个游戏在高中时期给我带来了很多欢乐.,虽然第一五星是大公(mmp)<br>
  但是时过境迁,fgo的游戏模式对于如今的我而言(是的我变心了,)太过于占用时间,所有我写了这个脚本,<br>
  使我可以在一边画画的同时挂机刷QB或者经验本,然后想了想,可能有与我一样的人,所有就发到github分享.<br>
  <br>
  至于大家认为的封号问题,其实这个脚本是我四月份写的,八月份更新的二代目.bilibili的视频其实也是一代目的<br> 
  我其实以及用了接近四个月了 ,刷了200+的金苹果 目前没有任何问题.
## 缺点声明

 战斗有点慢，可能需要三分一把。具体还是要看自己设置
目前只支持 助战：C阶
梅林
诸葛孔明
斯卡哈
C呆毛
## 功能
 目前适配两种模拟/
mate30 | 手机版本
2340*1080p 360 dip | 模拟器版本 

自动吃苹果，不能吃铜苹果（懒的写）
## 功能
 
- **自动助战**      √

- **技能选择**      √
   (从者技能以及御主技能)

- **自动选择色卡**  √

- **自动释放宝具**   √

- **自定义循环次数** √

> 本脚为自用，如果发生任何事情 ，作者不承担任何责任

### 项目部署
## 1.安装python 以及其需要库

  >python 自行百度安装 老简单了
 
 1-1.安装 python opencv库

  > 打开cmd 输入：
  > pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
  >
  > 打开cmd 输入：
  > pip install pip install uiautomator2

 1-2.查询opencv ,uiautomator2是否安装完成
 >输入 pip list 来查询是否安装成功

## 2.下载 并且解压 adb

你可以去自信下载 也可以直接使用下方链接进行我打包使用的adb

>[下载链接](https://pan.baidu.com/s/1nwqJXE5RKwXqRiFyxZ9OXQ)  提取码：gdqn

### 解压文件

![Image text](https://github.com/yiouna/fgo-Automated-combat/blob/main/images/1.jpg)

### 添加环境变量

此电脑 -> 右键 属性 -> 高级系统设置 -> 高级 -> 环境变量 -> 选择 Path -> 编辑 -> 新建 -> 输入解压根目录  

>这边我是放在了D:\dw\ADB 所以路径填写为 D:\dw\ADB
>

> 这个时候 打开你的手机 使用数据线连接电脑 adb devices 查询是否连接上
>adb devices   查询 安卓连接设备 连接设备
>![Image text](https://github.com/yiouna/fgo-Automated-combat/blob/main/images/7-1.jpg)
>代表连接成功

## ！使用模拟器方法连接 这里使用夜神模拟器 为例子
 ### 1.首先 先把上面的adb 步骤走完。
 ### 2.下载夜神模拟器。这个就不需要我教了
 ### 3.进入夜神根目录，看你安装在哪
>还记得之前下载的 adb 吗 复制一份 adb.exe 更名为 nox_adb.exe<br>
>Nox/bin <br>
 找到文件 nox_adb.exe 进行替换 同时把 Nox/bin 文件中自带的adb.exe 删除<br>
 然后重复环境变量操作 将nox_abd.exe 加入环境变量中<br>
 打开夜神模拟器。把分辨率调整为 2340x1080<br>
 在夜神模拟器中 打开usb调试<br>
>打开cmd（命令提示符）输入<br>
     >adb devices<br>
     >List of devices attached<br>
     >127.0.0.1:62001 device<br>
>就连接成功了<br>
 
 ## 下载本项目
 [fgo-Automated-combat](https://github.com/yiouna/fgo-Automated-combat)
 右上角 Code -> Download ZIP 进行下载
 
 ## 使用本项目
 
 建议下载一个 [Notepad](https://notepad-plus.en.softonic.com/download) 
 
 目录解构
    >fgo-Automated-combat-main
      >.idea
      >images
      >lib
      >config.py
      >main.py
      >README.md
      >zhilin.py
 我们进入文件 fgo-Automated-combat-main
 
 >手机或模拟器 停留在fgo 队伍确认界面<br>
 >打开 windows PowerShell<br>
 >python main.py<br>
 > 手动点击下 开始战斗，就开始战斗，自动过结算，自动继续循环关卡，自动选择助战。
 
 
 
# config.py 配置文件解释
  建议使用 Notepad 打开文件
  
  ## 战斗回合技能设置
  
  本脚本是自定义技能使用的 既多少回合结束战斗，每回合使用战斗技能，是否使用宝具，都需要自己进行填写，助战也是
  
    {
        'role_1': [[], 'false'],
        'role_2': [[], 'false'],
        'role_3': [[], 'false'],
        'master': [[], 'false'],
    },
      
 技能解读
    {
        'role_1': [{'fgo_huifu': "", 'fgo_baojuweili_up': ""}, 'true'],
        'role_2': [{'fgo_gongjili_up': "", 'fgo_baojuchongneng': "role_1", 'fgo_lanka_up': "role_1"}, 'false'],
        'role_3': [{'fgo_gongjili_up': "", 'fgo_baojuchongneng': "role_1", 'fgo_lanka_up': "role_1"}, 'false'],
        'master': [{'fgo_baojuchongneng': "role_1"}, 'false']
    },
    role_1 即为角色1
   
    {'fgo_huifu': "", 'fgo_baojuweili_up': ""}, 'true'
    回复技能,无目标  宝具威力加强,无目标  'true' 表示这回合使用宝具
    
    role_2 角色2 
    {'fgo_gongjili_up': "", 'fgo_baojuchongneng': "role_1", 'fgo_lanka_up': "role_1"}, 'false'
    攻击力加强 无目标 宝具充能 对象 一号角色 蓝卡加强 一号角色 不释放宝具
    
    masert 即为御主技能
    
    config 自动配备的 是小达芬奇 C呆毛 C呆毛 蓝卡队技能循环, 御主衣服为第二个技能是充能的衣服
       
       
![Image text](https://github.com/yiouna/fgo-Automated-combat/blob/main/images/%E6%8A%80%E8%83%BD.png)
# 声明

  任何因为本项目 而导致的账号损失，作者不负任何责任
     
