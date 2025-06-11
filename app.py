from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load saved model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_input = scaler.transform([features])
        prediction = model.predict(final_input)
        species = ['Setosa', 'Versicolor', 'Virginica'][prediction[0]]
        return render_template('index.html', prediction_text=f'Predicted Iris Species: {species}')
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.json
    features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    final_input = scaler.transform([features])
    prediction = model.predict(final_input)
    species = ['Setosa', 'Versicolor', 'Virginica'][prediction[0]]
    return jsonify({'prediction': species})

if __name__ == '__main__':
    app.run(debug=True)
