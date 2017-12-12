import pandas as pd
import numpy as np

data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/station0_New1_2.csv'))
data2 = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/station0_New_2.csv'))
data1 = np.loadtxt('C:/Users/a/Desktop/station0_2.csv',dtype=np.str,delimiter=',')
data3 = np.zeros([1,399])

sta =1
number = []
while sta < 400:
    n = 0
    b = data['SHEDID%d' % sta].sum()
    for a in data2['SHEDID%d'%sta]:
        if a !=' ':
            n += 1
        else:
            n += 0
    if b == 0:
        b = 0
        number.append(b)
    else:
        b = b/n
        number.append(b)
    sta += 1

data3[0] = number
all_data = np.r_[data1,data3]
df = pd.DataFrame(all_data,index=pd.date_range('2015/4/1','2015/9/1'),columns=range(1,400))
#df = pd.DataFrame(all_data,cloumn=range(1,400),index=pd.date_range('2015/4/1','2015/9/1'))
df.to_csv('C:/Users/a/Desktop/split_num.csv')


