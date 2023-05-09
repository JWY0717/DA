import pandas as pd
import csv

# txt 파일을 읽어와서 파싱하여 csv 형식으로 저장
with open('DA/data/ais.txt', 'r') as infile, open('ais.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for line in infile:
        # txt 파일의 구분자를 기준으로 데이터를 분리하여 리스트로 만듦
        data = line.strip().split('\t')
        # csv 파일에 데이터를 저장
        writer.writerow(data)



a = pd.read_csv('D:/장우영/LOCALSEARCH/PJ-Datamodel/DA/data/ais.csv', thousands=',',encoding='euc-kr')
print(a)
        
        