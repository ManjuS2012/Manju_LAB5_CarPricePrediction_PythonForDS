
# importing necessary libraries and functions
from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import sklearn
from sqlalchemy import true
from markupsafe import escape

#Initialize the flask App
app=Flask(__name__)
# loading the trained model  
model=pickle.load(open('model.pkl','rb'))

@app.route('/') #,methods=['GET']
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST']) 
def predict():
    if request.method == 'POST':
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Owner=int(request.form['Owner'])
        Fuel_Type=int(request.form['Fuel_Type'])
        Age_of_the_car=int(request.form['Age_of_the_car'])
        Seller_Type=int(request.form['Seller_Type'])
        Transmission=int(request.form['Transmission'])

        prediction=model.predict([np.array([Present_Price,Kms_Driven,Owner,Age_of_the_car,Fuel_Type,Seller_Type,Transmission])])
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text="You can sell your car at {} (In lakhs)".format(output))

if __name__=="__main__":
    app.run(debug=True)
