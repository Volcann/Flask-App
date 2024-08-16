from flask import Flask ,request ,jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/predict',methods=['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')

    input_query = np.array([[cgpa,iq,profile_score]])
    result = model.predict(input_query)[0]

    return jsonify({'result' : str(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

