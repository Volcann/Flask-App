from flask import Flask ,request ,jsonify
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/predict',methods=['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')

    input_query = pd.DataFrame([[cgpa, iq, profile_score]], columns=['cgpa', 'iq', 'profile_score'])
    result = model.predict(input_query)[0]
    return jsonify({'Placement': str(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
