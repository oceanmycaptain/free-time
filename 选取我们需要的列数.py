import pandas as pd
import numpy as np
'''选取我们需要的列并在列下面得到平均值和求和'''
chose_data1 = np.zeros([123,42])
# chose_data = [4, 94, 244, 245, 249, 279, 289, 293, 294, 327, 330, 334, 336, 342, 344, 348, 355, 356, 358, 359, 362, 363, 365, 366, 370, 373, 374, 375, 380, 383, 384, 386, 388, 389, 390, 391, 393, 395, 396, 397, 398, 399]
# data1 = []
# for a in chose_data:
#    data1.append('SHEDID%d'%a)


data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/station_date_1_drop_zero-del.csv'))
data3 = data.loc[(data['date']>='2015/4/1')]
#data3 = data2.loc[:,data1]

#data4 = data3.sum()/123
#data3.loc['number'] = data3.apply(lambda x:(x.sum()))#可以在我们的数据下加上一行我们得到的数据，加列的话就加上axis = 1
data3 = pd.DataFrame(data3)
data3.to_csv('C:/Users/a/Desktop/station0_New_2.csv')



