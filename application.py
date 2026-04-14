import os
print("Current Working Directory:", os.getcwd())
print("Templates Folder Exists:", os.path.exists('templates'))
print("Templates Content:", os.listdir('templates') if os.path.exists('templates') else "Not Found")



from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templetes')

app = Flask(__name__, template_folder=template_dir)

# Load models
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        # Get form values (match EXACT names from HTML)
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Class = float(request.form.get('Class'))
        Region = float(request.form.get('Region'))

        # Prepare input
        input_data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Class, Region]])

        # Scale
        scaled_data = standard_scaler.transform(input_data)

        # Predict
        prediction = ridge_model.predict(scaled_data)[0]

        return render_template('index.html', result=round(prediction, 2))

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)