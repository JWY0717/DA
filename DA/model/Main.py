import pandas as pd
import numpy as np


excel_file = 'D:/장우영/LOCALSEARCH/ShipMovementPrediction_Project/teamproject-main/DA/data/해양기상_통계자료_신항유도등.xls'

df = pd.read_excel(excel_file)
#   print(df.shape)

# 데이터 확인 
#print(df)
#print(df.head(5))

# 결측치 제거
df.dropna(inplace=True)
#print(df.head(5))


with open('ais.txt', 'r') as file:
    # Read the entire contents of the file
    content = file.read()


print(content)
