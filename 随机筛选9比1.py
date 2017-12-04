import pandas as pd
import numpy as np
import random
import json
from sklearn.cross_validation import train_test_split

data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/Nozero_station2.csv'))
#print(data)
data_all = {}
sta = 1
while sta<400:#代表着到多少个车位
    data2 = [4, 94, 244, 245, 249, 279, 289, 293, 294, 327, 330, 334, 336, 342, 344, 348, 355, 356, 358, 359, 362,
             363, 365, 366, 370, 373, 374, 375, 380, 383, 384, 386, 388, 389, 390, 391, 393, 395, 396, 397, 398, 399]
        #需要排除的车位数
    if sta not in data2:
        data1 = data['%d'%sta]
        list1 = []
        for a in data1:
            if a != ' ':
                list1.append(a)
        c = []
        num = len(list1)//10
        if num != 0:
            random_list1,random_list2 = train_test_split(list1,test_size=0.1)
            #分出是10份
            for i in range(0,len(random_list1),num):
                b = random_list1[i:i+num]
                c.append(b)
                c.append(random_list2)
            data_all[sta] = c
            sta += 1
                #print(data_all)
        else:
            sta += 1
    else:
        sta += 1
#print(data_all)
file = open('C:/Users/a/Desktop/456.json','w')
jsObj = json.dumps(data_all)
file.write(jsObj)
file.close()
# print(list1)
# print(len(list1))
# a1 = len(list1)//10
# print(a1)
# random_list1 = random.sample(list1,9*a1)
# #random_list2 = data1
# random_list2 = list(set(list1).difference(set(random_list1)))
# print(random_list2)






