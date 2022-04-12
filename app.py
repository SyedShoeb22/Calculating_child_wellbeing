from flask import Flask
import pickle
from flask import render_template
from flask import request
import pandas as pd
import numpy as np
model=pickle.load(open(r'S:\DATA SCIENCE\DS Project\flask\xgb1_model.pkl','rb'))

# application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

 # , methods = ['POST']
@app.route('/result' , methods = ['POST'])
def result():
    final_features = [int(x) for x in request.form.values()]
    final_features = [np.array(final_features)]
    prediction = model.predict(final_features)

    return render_template('Home.html', output='Child status is :  {}'.format(prediction[0]))


if __name__ == "__main__":
    app.run(debug=True)









