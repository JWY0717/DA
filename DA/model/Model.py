# 입력으로는 시간에 따른 선박의 위치 정보와 해당 시간의 기상 데이터를 사용하고, 
# 출력으로는 다음 시간대의 선박 위치 정보를 예측합니다.

import pandas as pd
import csv


excel02_file = 'D:/장우영/LOCALSEARCH/DA/log.csv'

df = pd.read_excel(excel02_file)
#   print(df.shape)

# 데이터 확인 

print(df.head(1))