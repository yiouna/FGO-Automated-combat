# Automated combat
一个  python 刷狗粮脚本。 使用opencv库

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
  > 进行安装

 1-2.查询opencv是否安装完成
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
  
     [{'role_1': [['a','b'], c, ‘d’],
      'role_2': [['a','b'], c, ‘d’]，
      'role_3': [['a','b'], c, ‘d’]，
      'master': [['a','b'], c, ‘d’]，}]
      
      如此便代表一回合
     
     [{'role_1': [['a','b'], c, ‘d’],
      'role_2': [['a','b'], c, ‘d’]，
      'role_3': [['a','b'], c, ‘d’]，
      'master': [['a','b'], c, ‘d’]，},
      {'role_1': [['a','b'], c, ‘d’],
      'role_2': [['a','b'], c, ‘d’]，
      'role_3': [['a','b'], c, ‘d’]，
      'master': [['a','b'], c, ‘d’]，}]
      
      如此便代表两回合
      
      a b 代表的是技能 只需要参照技能图标进行填写即可 如果不使用技能留空则好
      
      c 则是是否使用宝具。 False 不使用 True 使用
      d 则是 技能使用 如果需要对角色进行选择 则填写 role_1 role_2 role_3 
        如果不需要 则填写 None （目前只支持一个角色的技能针对 一个角色
        
       'role_1': [['fgo_baojuchongneng'], False, 'role_2']
       
       翻译 角色1 使用宝具充能技能，  不使用宝具 技能对角色2 使用
       
       'role_2': [[], False, None],
        
       翻译 角色2 不适用技能 不使用宝具 技能不会任何人使用
       
# 声明

  任何因为本项目 而导致的账号损失，作者不负任何责任
     
