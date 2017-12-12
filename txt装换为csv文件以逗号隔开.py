import pandas as pd

df = open('C:/Users/a/Desktop/park.txt','r')
data = []
for line in df:
    line = line.strip('\n')
    line = line.split(',')
    data.append(line)

data = pd.DataFrame(data)
data.to_csv('C:/Users/a/Desktop/park123.csv')



