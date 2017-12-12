import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''本次从十几万条的数据中，得到我们的SHEDID和RTSHEDID的之间的数量关系，这次我采用的是
填充（读一个我们就填进去）的方式，遍历（读完一遍找到每次我们要的）的话就相当慢了。
后面的程序是为了画我们的三维图'''
all_data = np.zeros([399,399])
#data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/train2.csv'))
data = np.loadtxt('C:/Users/a/Desktop/train2.csv',dtype=np.str,delimiter=',')
for i in range(1,len(data)):
    SHE = int(data[i][3])
    RTSHE =int(data[i][4])
    all_data[SHE-1][RTSHE-1] += 1#行为SHE的行为，列为RTSHE的行为。
#data2 = pd.DataFrame(all_data,index=range(1,400),columns=range(1,400))
#data2.to_csv('C:/Users/a/Desktop/111.csv')
#print(all_data)
z = all_data
x = np.arange(1,400,1)
y = np.arange(1,400,1)
x,y = np.meshgrid(x,y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z,cmap='rainbow')
# z = all_data
plt.show()



