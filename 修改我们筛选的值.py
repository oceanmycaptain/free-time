import pandas as pd
'''此次我们需要将我们的csv文件的部分需要改变的车站的RT和LEASE值进行改变'''
changedata = [ 94, 244, 245, 249, 279, 289, 293, 294, 327, 330, 334, 336, 342, 344, 348, 355,356, 358, 359, 362, 363,
      365, 366, 370, 373, 374, 375, 380, 383, 384, 386, 388, 389, 390, 391, 393, 395, 396, 397, 398, 399]
data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/result.csv'))
for number in changedata:
    data[data['SHEDID']==number]=data[data['SHEDID']==number].replace({'LEASE':data['LEASE'][data['LEASE']==0],'RT':data['RT'][data['RT']==0]},1)
    #data[data['SHEDID']==number].replace({'LEASE':data['LEASE'][data['LEASE']==0],'RT':data['RT'][data['RT']==0]},1)
    #不知道为什么我用这种方法实现不了，我想要的要求。问题一直没有相同，与上面的差别不算很大吧
data.to_csv('C:/Users/a/Desktop/12346.csv')
#example=pd.read_csv('C:/Users/a/Desktop/12.4 xgb_0.06215.csv')
#print(example)
#example=example.replace({'LEASE':example['LEASE'][example['LEASE']<=3],'RT':example['RT'][example['RT']<=3]},4)
#将列表的值筛选并进行更换
#example[example['RT']==3]
#example.to_csv('C:/Users/Mr.Handsome/Desktop/12.4.csv',index=False)