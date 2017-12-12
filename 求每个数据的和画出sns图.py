import pandas as pd
import numpy as np
pd.set_option('display.max_row',None)
pd.set_option('display.max_columns',None)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid',color_codes=True)
sns.set(font_scale=1.4)
color = sns.color_palette()


data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/Newstation_data.csv'))
sta_num = np.zeros([399,1])
#sta_num = []
for sta in range(1,400):
    #sta_num.append(sum(data['%d'%sta]))
    sta_num[sta-1][0]=sum(data['%d'%sta])
#print(sta_num)
sns.set(font_scale=1.8)
plt.figure(figsize=(20,10))
ax = sns.distplot(sta_num,bins=100,kde=True,color='b',kde_kws={'lw':3,'label':'all'},hist=False)
plt.title('sta')
plt.show()