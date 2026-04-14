from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application

#import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():

    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
            # Get input values
            data = [
                float(request.form.get('temperature')),
                float(request.form.get('rh')),
                float(request.form.get('ws')),
                float(request.form.get('rain')),
                float(request.form.get('ffmc')),
                float(request.form.get('dmc')),
                float(request.form.get('isi')),
                float(request.form.get('classes')),
                float(request.form.get('region'))
            ]

    else:
        return render_template('home.')
if __name__=='__main__':
    app.run(host='0.0.0.0')
