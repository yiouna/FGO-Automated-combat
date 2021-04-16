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

  >python 自信百度安装 老简单了
 
 1-1.安装 python opencv库

  > 打开cmd 输入：
  > pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-contrib-python
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
>还记得之前下载的 adb 吗 复制一份 adb.exe 更名为 nox_adb.exe
>Nox/bin 
 找到文件 nox_adb.exe 进行替换 同时把 Nox/bin 文件中自带的adb.exe 删除
 然后重复环境变量操作 将nox_abd.exe 加入环境变量中
 打开夜神模拟器。把分辨率调整为 2340x1080
 在夜神模拟器中 打开usb调试
>打开cmd（命令提示符）输入
     >adb device
     >List of devices attached
     >127.0.0.1:62001 device
>就连接成功了
 
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
 
 > 手机或模拟器 停留在fgo 队伍确认界面
 >打开 windows PowerShell
 >python main.py
 > 手动点击下 开始战斗，就开始战斗，自动过结算，自动继续循环关卡，自动选择助战。
 
 
