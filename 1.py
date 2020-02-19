import numpy as np
from numpy import *
import fun1
file1 = open("D2z.txt", "r")
text = file1.read()
text1 = text.split()
#text2 = [1,2]
#print(len(text2))
num = []
labels = []
for j in range(0, 200):
    for k in range(0, 3):
        if(k == 0):
            num.append([])
        if(k == 0 or k == 1):
            num[j].append(float(text1[3 * j + k]))
        if(k == 2):
            labels.append(int(text1[3 * j + k]))
num = np.array(num)
labels = np.array(labels)

file2 = open("test.txt", "r")
text2 = file2.read()
text22 = text2.split()
test = []
for j in range(0, 200):
    for k in range(0, 2):
        if(k == 0):
            test.append([])
        if(k == 0 or k == 1):
            test[j].append(float(text22[3 * j + k]))
test = np.array(test)





for i in range(int(len(test)/2)):
    print(test[i], fun1.kNN_Classify(test[i], num, labels, 1))



file1.close()
file2.close()