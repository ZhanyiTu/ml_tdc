import numpy as np
file1 = open("D2z.txt", "r")
text = file1.read()
print(text)
text1 = text.split()
print(text1)
#text2 = [1,2]
#print(len(text2))
num = []
for j in range(0, 200):
    for k in range(0, 3):
        if(k == 0):
            num.append([])
        num[j].append(text1[3 * j + k])
print(num)

file1.close()