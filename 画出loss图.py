import numpy as np
import pandas as pd
pd.set_option('display.max_row',None)
pd.set_option('display.max_columns',None)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid',color_codes=True)
sns.set(font_scale=1.4)
color = sns.color_palette()

file = '12.6-7-501-1-lea.csv'
num1 = 8
num2 = 9
num3 = 10
#num4 = 15
Attributes = 'n_cv'

feature_fraction = pd.read_csv('C:/Users/a/Desktop/lea/%s'%file)
feature_fraction_num1 = feature_fraction[feature_fraction['%s'%Attributes]==num1]
feature_fraction_num2 = feature_fraction[feature_fraction['%s'%Attributes]==num2]
feature_fraction_num3 = feature_fraction[feature_fraction['%s'%Attributes]==num3]
#feature_fraction_num4 = feature_fraction[feature_fraction['%s'%Attributes]==num4]

x1 = 'lowest_valid_loss'

sns.set(font_scale=1.8)
plt.figure(figsize=(15,8))
ax1 = sns.distplot(feature_fraction_num1['%s'%x1],bins=100,kde=True,color='b',kde_kws={'lw':3,'label':num1},hist=False)
ax2 = sns.distplot(feature_fraction_num2['%s'%x1],bins=100,kde=True,color='r',kde_kws={'lw':3,'label':num2},hist=False)
ax3 = sns.distplot(feature_fraction_num3['%s'%x1],bins=100,kde=True,color='y',kde_kws={'lw':3,'label':num3},hist=False)
#ax4 = sns.distplot(feature_fraction_num4['lowest_valid_loss'],bins=100,kde=True,color='g',kde_kws={'lw':3,'label':num4},hist=False)
plt.title('rt of %s'%x1)
plt.ylim(0,6)
#plt.show()
fig = plt.gcf()
fig.savefig('C:/Users/a/Desktop/lea/%s-%s.png' %(file,Attributes), pdi=1000, bbox_inches='tight')
plt.close()