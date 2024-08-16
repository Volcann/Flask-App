import os
from flask import Flask, request, jsonify
import pickle
import numpy as np  # Make sure numpy is imported
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load your model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if data:
        cgpa = data.get('cgpa')
        iq = data.get('iq')
        profile_score = data.get('profile_score')
    else:
        cgpa = request.form.get('cgpa')
        iq = request.form.get('iq')
        profile_score = request.form.get('profile_score')

    # Convert inputs to float and handle missing values
    try:
        cgpa = float(cgpa)
        iq = float(iq)
        profile_score = float(profile_score)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input. Please provide numeric values.'}), 400

    try:
        input_query = np.array([[cgpa, iq, profile_score]])
        result = model.predict(input_query)[0]
        return jsonify({'result': str(result)})
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

