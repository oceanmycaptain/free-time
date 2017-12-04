import pandas as pd
import numpy as np
import random
import json
'''此次的要求是将数据随机分割10份，无法平分就9等份和1份大的，还有部分数据我们再读的时候规定删除，
和之前的用的from sklearn.cross_validation import train_test_split包差不多，但此时我用的是list-random
的方法'''
data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/Nozero_station2.csv'))
#print(data)
all_data={}
for sta in range(1,400):
    data2 = [4, 94, 244, 245, 249, 279, 289, 293, 294, 327, 330, 334, 336, 342, 344, 348, 355, 356, 358, 359, 362,
             363, 365, 366, 370, 373, 374, 375, 380, 383, 384, 386, 388, 389, 390, 391, 393, 395, 396, 397, 398, 399]
    if sta not in data2:
        list1 = []
        for a in data['1']:
            if a != ' ':
                list1.append(a)
        a1 = len(list1)//10
        if a1 != 0:
            a3 = []
            random_list1 = random.sample(list1,9*a1)
            for slist in range(0,len(random_list1),a1):#分成相应的9等份
                a2 = random_list1[slist:slist+a1]
                a3.append(a2)
            c = list1
            for b in random_list1:#导出每个我们随机到的，并且在下面的进行删除，得到我们剩下的
                c.remove(b)
            a3.append(c)
            all_data[sta] = a3
file = open('C:/Users/a/Desktop/4567.json', 'w')
jsObj = json.dumps(all_data)
file.write(jsObj)
file.close()





#random_list2 = list(set(list1).difference(set(random_list1)))
# print(random_list2)
