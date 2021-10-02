from flask import Flask, request
from flask_cors import CORS, cross_origin
import cv2
import requests
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    img = request.files['img']

    filename = './uploads/{}'.format(img.filename)
    img.save(filename)

    img = cv2.imread(filename)
    array = cv2.resize(img, (100, 100)) / 255
    data = json.dumps({
        'signature_name': 'serving_default',
        'instances': array.reshape(-1, 100, 100, 3).tolist()
    })

    url = 'http://localhost:8501/v1/models/test:predict'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    if response.status_code != 200:
        return {'message': 'error: something went wrong'}, 500

    result = response.json()['predictions'][0][0]
    return {'result': str(result)}, 200

if __name__ == '__main__':
    app.run(debug=True)
