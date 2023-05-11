# 입력으로는 시간에 따른 선박의 위치 정보와 해당 시간의 기상 데이터를 사용하고, 
# 출력으로는 다음 시간대의 선박 위치 정보를 예측합니다.

import numpy as np
import pandas as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

# AIS 데이터와 기상 데이터를 불러와 입력 데이터와 출력 데이터를 구성합니다.
# 입력 데이터는 (시간, AIS 데이터 차원 + 기상 데이터 차원)의 2D 배열 형태를 갖습니다.
# 출력 데이터는 (시간, AIS 데이터 차원)의 2D 배열 형태를 갖습니다.
X_train, y_train, X_val, y_val = load_data()

# LSTM 모델을 생성합니다.
model = Sequential()
model.add(LSTM(64, input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32))
model.add(Dropout(0.2))
model.add(Dense(y_train.shape[1]))

# 모델을 컴파일합니다.
model.compile(loss='mean_squared_error', optimizer='adam')

# 모델을 학습시킵니다.
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, batch_size=64)