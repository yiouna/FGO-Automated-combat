import zhilin, random
import numpy as nu
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../images/02-1 (2).png')


img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([]),plt.yticks([])
plt.show()

"""
295 757  608 927
688 757  973 927
1045 757    1372 927
1148 757    1769 927
1832  757  2146 927
"""
"""
x 800 y 300
900  400

x 1150 y 300
1250   400


x 880  1400
y 400  500
"""

