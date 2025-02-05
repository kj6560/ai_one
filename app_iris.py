from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import logging
import os
from logging.handlers import RotatingFileHandler
app = Flask(__name__)

try:
    # Load the trained model
    model = joblib.load('iris_model.pkl')
    app.logger.info("Model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading model: {e}")

@app.route('/')
def home():
    app.logger.info("Home route accessed.")
    return render_template('index.html')  # Corrected template path

@app.route('/predict', methods=['POST'])
def predict():
    app.logger.info("Predict route accessed.")
    try:
        # Get the data from the POST request
        data = request.get_json(force=True)
        app.logger.debug(f"Data received: {data}")

        # Convert data into numpy array
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction using the model
        prediction = model.predict(features)
        
        # Map the prediction to the corresponding species
        species = ['setosa', 'versicolor', 'virginica']
        result = species[prediction[0]]
        
        # Return the result as a JSON response
        app.logger.debug(f"Prediction result: {result}")
        return jsonify({'prediction': result})
    except Exception as e:
        app.logger.error(f"Error in prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Corrected the condition to run the app