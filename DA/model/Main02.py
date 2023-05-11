import pandas as pd
import csv

# txt 파일을 읽어와서 파싱하여 csv 형식으로 저장
with open('DA/data/time.txt', 'r') as infile, open('time.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for line in infile:
        # txt 파일의 구분자를 기준으로 데이터를 분리하여 리스트로 만듦
        data = line.strip().split('\t')
        # csv 파일에 데이터를 저장
        writer.writerow(data)



a = pd.read_csv('time.csv', thousands=',',encoding='euc-kr')
#print(a)


with open('time.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        fields = row[0].split(' ')
        time = fields[1] + ' ' + fields[2]
        mmsi = fields[4]
        posX = fields[8]
        posY = fields[10]
        print(f'time: {time}, mmsi: {mmsi}, posX: {posX}, posY: {posY}')
        
from datetime import datetime

date_str = '5/9/2023'
date_obj = datetime.strptime(date_str, '%m/%d/%Y')
formatted_date = date_obj.strftime('%Y-%m-%d')

print(formatted_date) 
        
        
        
# time: 5/9/2023, 17:50:46, mmsi: 636018242, posX: MSC, posY: VI