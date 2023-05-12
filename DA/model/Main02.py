import pandas as pd
import csv

df = pd.read_csv('D:/장우영/LOCALSEARCH/DA/log.csv')
#print(df)
print(df.head(1))


#with open('log.csv', 'r') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        fields = row[0].split(' ')
#        time = fields[0] + fields[1] + ','+  fields[2]
#        posX = fields[5]
#        posY = fields[6]
#        print(f'{time},posX: {posX}, posY: {posY}')



#time:5/9/2023, 17:11:10 mmsi:413219020 shipType:70 shipName:ZHONG WAI YUN NINGBO posX:129.30875714057603 posY:34.97518208647576

