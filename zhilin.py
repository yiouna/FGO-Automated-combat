import os


def png(x):
    os.system(f'{x} shell screencap /sdcard/02.png')
    os.system(f'{x} pull /sdcard/02.png images/zhandou.png')