import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 
data = pd.read_csv('ship_location.csv')
    
# 풍향,유향,기온,풍속,유속,기압,습도 를 독립 변수
X = data[['temperature', 'wind_speed', 'wave_height']]

# 선박의 위치(위도, 경도)를 종속 변수
y = data['ship_speed']
    
# 데이터 셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
# 선형 회귀 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)
    
# 테스트 데이터에 대한 예측
y_pred = model.predict(X_test)
    
# 모델 성능 평가
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print('R2 score:', r2)
print('Mean squared error:', mse)
    
# Basemap을 사용하여 지도 상에 예측값을 시각화합니다.
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='merc', llcrnrlat=10, urcrnrlat=70, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
m.fillcontinents(color='#CCCCCC', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')
x, y = m(X_test['longitude'].tolist(), X_test['latitude'].tolist())
m.scatter(x, y, marker='o', s=y_pred*10, alpha=0.5, edgecolor='black')
plt.title('Predicted Ship Speed by Location')
plt.show()