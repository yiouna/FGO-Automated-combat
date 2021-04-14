import os


def png():
    os.system('adb shell screencap /sdcard/02.png')
    os.system('adb pull /sdcard/02.png images/zhandou.png')