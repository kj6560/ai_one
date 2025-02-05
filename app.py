# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('iris_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Convert data into numpy array
    features = np.array(data['features']).reshape(1, -1)
    
    # Make prediction using the model
    prediction = model.predict(features)
    
    # Map the prediction to the corresponding species
    species = ['setosa', 'versicolor', 'virginica']
    result = species[prediction[0]]
    
    # Return the result as a JSON response
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)