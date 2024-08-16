import os
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load your model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
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

    input_query = np.array([[cgpa, iq, profile_score]])
    result = model.predict(input_query)[0]

    return jsonify({'result': str(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
