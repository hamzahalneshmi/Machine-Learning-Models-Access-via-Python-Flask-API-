# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json

app = Flask(__name__)
# Load the model
model = pickle.load(open(r'rainfull.pkl','rb'))
@app.route('/rainfull',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(data)
    start = json.dumps(data["start"])
    end = json.dumps(data["end"])
    prediction = model.predict(int(start), int(end))
    jsonStr = json.dumps(prediction.values.tolist())
    return jsonify(jsonStr)
if __name__ == '__main__':
    app.run(port=5003, debug=True)