from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)


def predict_diabetes(row):
    prediction = model.predict([row])
    return 'Positive' if prediction[0] == 1 else 'Negative'


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    row = pd.Series(data)
    result = predict_diabetes(row)
    return jsonify({'prediction': result})


if __name__ == '__main__':
    app.run(debug=True)
