import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    if output:
        o = ""
    else:
        o="not "

    return render_template('home.html', prediction_text='Water is {}potable.'.format(o))


if __name__ == "__main__":
    app.run(debug=True)