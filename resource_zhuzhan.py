# -*- coding: utf-8 -*-
# @Time : 2021/8/16 23:53
import cv2 as cv

#资源加载

# 助战刷新.确认
fgo_zhuzhan_shuaxing = cv.imread("images/system/fgo_zhuzhan_shuaxing.png")
fgo_zhuzhan_shuaxing_OK = cv.imread("images/system/fgo_zhuzhan_OK.png")


# 坐标排列方式 x_1, x_2, y_1, y_2,
shouji_mate30 = [[700, 250, 930, 800],
                [1160, 770, 930, 800],
                [1640, 1200, 930, 800],
                [1940, 1550, 630, 400]]

#2340 - 1080
moniqi_1 = [[700, 250, 930, 800],
            [1160, 720, 930, 800],
            [1640, 1200, 930, 800],
            [1892, 1474, 537, 392]]
