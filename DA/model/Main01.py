import pandas as pd
import numpy as np

excel_file = 'D:/장우영/LOCALSEARCH\DA\DA\data/05_09해양 기상청 데이터.xls'

df = pd.read_excel(excel_file)
#   print(df.shape)

# 데이터 확인 
print(df)
#print(df.head(5))
#print(df.shape)

# 결측치 제거
df.dropna(inplace=True)
#print(df.head(5))

#  지방청            표지                일시023-05-09 17:40	2	     168	    15.8	 4.11	    0.4		             73
#  부산청	부산항유도등부표(랜비)	2023-05-09 17:30	5	     178	    16	     4.11	    0.2		             68
#  부산청	부산항유도등부표(랜비)	2023-05-09 17:20	7	     196        15.8	 3.08	    0.3		             68
#  부산청	부산항유도등부표(랜비)	2023-05-09 17:10	266	     105	    16.4	 2.57	    0.1		             74
#  부산청	부산항유도등부표(랜비)	2023-05-09 17:00         풍향(˚)  유향(˚)  기온(℃)  풍속(m/s)  유속(kn)   기압(hPa)   습도(%)
#  부산청	부산항유도등부표(랜비)	2	219	     210	    16.5	 4.63	    0.1		             74
