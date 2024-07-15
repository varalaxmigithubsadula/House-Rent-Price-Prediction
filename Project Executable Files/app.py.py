import numpy as np

import pickle

from flask import Flask, request, render_template

app=Flask(__name__, template_folder="templates")

model =pickle.load(open(r'C:\Users\Anitha\Downloads\House  Rent Price Prediction using Machine Learning\Flask\mini.pkl','rb'))

@app.route('/')

def home():

    return render_template('index.html')


@app.route('/index')

def index():
    return render_template('index.html')



@app.route('/Prediction', methods=['GET','POST'])


def predict():

    return render_template('Prediction.html')

@app.route('/result', methods=['POST'])

def result():
    
    input_features = [float(x) for x in request.form.values()]
                     
    features_value= [np.array(input_features)]

    print(features_value)

    #Features_name = ['city', 'BHKS', 'sqft_per_inch', 'build_up_area', 'Type_of_property', 'deposit'] 
    
    prediction = model.predict(features_value)

    output=prediction[0] #np.exp(predictions)

    #output = np.exp(output)

    #output = np.round(output) 
    
    print(output)

    return render_template('result.html', dt= 'House Rent is {}'.format(output))

if __name__=='__main__':
    
     app.run(debug=True)