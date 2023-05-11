import pandas as pd
import numpy as np

excel_file = 'D:/장우영/LOCALSEARCH/ShipMovementPrediction_Project/teamproject-main/DA/data/해양기상_통계자료_신항유도등.xls'

df = pd.read_excel(excel_file)
#   print(df.shape)

# 데이터 확인 
print(df)
#print(df.head(5))
#print(df.shape)

# 결측치 제거
df.dropna(inplace=True)
#print(df.head(5))

#     지방청            표지                    일시            풍향(˚)  유향(˚)  기온(℃)  풍속(m/s)  유속(kn)  기압(hPa)  습도(%)
#    부산청  부산항유도등부표(랜비)         2023-05-08 23:50      0        189     14.4       3.08      0.9      1015.0     57
 