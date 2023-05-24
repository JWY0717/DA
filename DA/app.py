import pandas as pd
import numpy as np
import pickle
from pyproj import Transformer
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open('DA/notebooks/linear_regression_model.pkl', 'rb'))

#Load the coordinate transformer
transformer = Transformer.from_crs(3857, 4326, always_xy=True)

def convert_coordinates(coord):
        # 빈 문자열인 경우 처리
    if not coord:
        return None 

    try:
        # 좌표값을 파싱하여 x, y 좌표 추출
        x = int(coord[8:24], 16) / 10000000.0
        y = int(coord[24:40], 16) / 10000000.0

        # 좌표 변환
        lon, lat = transformer.transform(x, y)

        return lon, lat
    except ValueError:
        # 유효하지 않은 형식의 좌표값인 경우 처리
        return None

@app.route('/predict', methods=['POST'])
def predict():
    # Get the request data
    data = request.get_json()

    # Preprocess the input data
    input_data = pd.DataFrame(data["data"])
    input_data['geom'] = input_data['geom'].apply(convert_coordinates)
    input_data['경도'] = input_data['geom'].apply(lambda x: x[0] if x is not None else None)
    input_data['위도'] = input_data['geom'].apply(lambda x: x[1] if x is not None else None)
    input_data['insert_time'] = pd.to_datetime(input_data['insert_time']).astype('int64') // 10**9

    # Select the features for prediction (excluding 'geom') !!!
    features = ["mmsi", "ship_type", "경도", "위도", "cog", "sog", "insert_time", "풍향", "유향", "기온", "수온", "풍속", "유속", "기압", "습도"]
    input_data = input_data[features]
    
    # Make predictions
    predictions = model.predict(input_data)

    # Prepare the response
    response = {"predictions": predictions.tolist()}

    return jsonify(response)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)



