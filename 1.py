import numpy as np
from numpy import *
import fun1
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
file1 = open("D2z.txt", "r")
text = file1.read()
text1 = text.split()
#text2 = [1,2]
#print(len(text2))
num = []
labels = []
x1value = []
x2value = []
y1value = []
y2value = []
for j in range(0, 200):
    for k in range(0, 3):
        if(k == 0):
            num.append([])
            num[j].append(float(text1[3 * j + k]))
        if (k == 1):
            num[j].append(float(text1[3 * j + k]))
        if(k == 2):
            labels.append(int(text1[3 * j + k]))
            if(int(text1[3 * j + k]) == 0):
                x1value.append(float(text1[3 * j + k - 2]))
                y1value.append(float(text1[3 * j + k - 1]))
            if (int(text1[3 * j + k]) == 1):
                x2value.append(float(text1[3 * j + k - 2]))
                y2value.append(float(text1[3 * j + k - 1]))
num = np.array(num)
labels = np.array(labels)

file2 = open("test.txt", "r")
text2 = file2.read()
text22 = text2.split()
print(text22)
test = []
x21value = []
x22value = []
y21value = []
y22value = []
print(int(len(text22) / 2))
for j in range(int(len(text22) / 2)):
    for k in range(0, 2):
        if(k == 0):
            test.append([])
        if(k == 0 or k == 1):
            test[j].append(float(text22[2 * j + k]))
test = np.array(test)
print(test)
for i in range(int(len(test))):
    value = fun1.kNN_Classify(test[i], num, labels, 1)
    if(value == 0):
        x21value.append(float(test[i][0]))
        y21value.append(float(test[i][1]))
    if(value == 1):
        x22value.append(float(test[i][0]))
        y22value.append(float(test[i][1]))



font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

xValue = list(range(0, 101))
yValue = [x * np.random.rand() for x in xValue]

plt.title(u'散点图示例', FontProperties=font)

plt.xlabel('x-value')
plt.ylabel('y-label')
# plt.scatter(x, y, s, c, marker)
# x: x轴坐标
# y：y轴坐标
# s：点的大小/粗细 标量或array_like 默认是 rcParams['lines.markersize'] ** 2
# c: 点的颜色
# marker: 标记的样式 默认是 'o'
plt.legend()

plt.scatter(x1value, y1value, s=20, c="#ff1212", marker='o')
plt.scatter(x2value, y2value, s=20, c='#0000FF', marker='o')
plt.scatter(x21value, y21value, s=20, c="#ff1212", marker='v')
plt.scatter(x22value, y22value, s=20, c='#0000FF', marker='v')
plt.show()





file1.close()
file2.close()