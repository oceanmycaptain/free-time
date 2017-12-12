import pandas as pd
'''需要得到我们筛选的列并且在pandas中将数据改变'''
data1 = pd.read_csv('C:/Users/a/Desktop/workspace_2/result_new.csv')
data2 = pd.read_csv('C:/Users/a/Desktop/combine_new.csv')
print(data2)
sta = []
for a in data2['sta']:
    sta.append(a)
print(sta)
loss = []
for b in data2['number']:
    loss.append(b)
print(loss)
data3 = data1.copy()
for n in range(0,99):
    tem = data3[data3['SHEDID']==sta[n]]['LEASE'].as_matrix() * loss[n]#需要将pandas用matrix改为矩阵
    data3.loc[data3['SHEDID']==sta[n],'LEASE'] = tem
new_data = pd.DataFrame(data3)
new_data.to_csv('C:/Users/a/Desktop/change_data_NEW.csv')





#data = data1.loc[(data1['SHEDID']=)]