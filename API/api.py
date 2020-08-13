from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import joblib
from firebase import firebase
from sklearn.preprocessing import PolynomialFeatures
import tensorflow as tf
import keras

app = Flask(__name__)
api = Api(app)

# Load Models
# 5 models
RFM_model = joblib.load('saved_Models/RandomForestClassifier_model.sav') # Random Forest 
LRM_model = joblib.load('saved_Models/LogisticRegression.sav') # Logistic regression
SGDCM_model = joblib.load('saved_Models/SGDC.sav') # Stochastic gradient descent
SVCM_model = joblib.load('saved_Models/svcmodel.sav') # Support vector machine
NNM_model = keras.models.load_model('saved_Models/NNM.h5') # Artificial neural network
RNM_model = keras.models.load_model('saved_Models/RNN.h5') # Recurrent neural network

# fireBase Link
firebase = firebase.FirebaseApplication('https://drive-behaviour.firebaseio.com/',None) # if there is no link will return None

# -Reformat dataset to create windows with size 60 to create time sequence
# -That is because of the output of the current record does 
# not depend on the current input only but also the previous sequence (time sequence)
# RNN
def createWindows(X):
    features_set = []
    W_SIZE = 60
    LENGTH = len(X)

    for i in range(W_SIZE,LENGTH):
        try:
            xx = X[i-W_SIZE:i,:]
            xx = np.array(xx)
            features_set.append(xx)
        except:
            print("error in i = ",i)
    return np.array(features_set) 

# load data from fireBase
def get_data(degree):
    result = firebase.get('/DriveBehaviour',None) # if there is no bath will return None
    X_data = []

    # iterate in a result that came from firebase to get sensor data
    if result != None:
        for key in result:
            X_data.append([result [key]['_1X_Acelerometro'] ,
                  result [key]['_1Y_Acelerometro'] ,
                  result [key]['_1Z_Acelerometro'] ,
                  result [key]['_2X_Giroscope'] ,
                  result [key]['_2Y_Giroscope'] ,
                  result [key]['_2Z_Giroscope']])

    # Convert X_data to numby array 
    X_data = np.array(X_data)

    # increase data features 
    poly = PolynomialFeatures(degree=degree , include_bias=False)
    X=poly.fit_transform(X_data)

    return X

# get events percent
def count(predictions):
    counter = {
            1.0:0,
            2.0:0,
            3.0:0,
            4.0:0,
            5.0:0,
            6.0:0,
        }
    for y in predictions:
      counter[y] = counter[y]+1

    for k in counter:
        counter[k] = ( counter[k] / len(predictions) )*100 
        counter[k] = round(counter[k] , 2) 

    return counter

# Random Forest 
class RFM (Resource):
    def get(self):
        # get data
        X = get_data(2)
        # get predection
        predictions = RFM_model.predict(X)
        # return predected events percent   
        return count(predictions)

# Logistic regression
class LRM (Resource):
    def get(self):
        # get data
        X = get_data(5)
        # get predection
        predictions = LRM_model.predict(X)
        # return predected events percent
        return count(predictions)

# Stochastic gradient descent
class SGDC (Resource):
    def get(self):
        # get data
        X = get_data(2)
        # get predection
        predictions = SGDCM_model.predict(X)
        # return predected events percent
        return count(predictions)

# Support vector machine
class SVC (Resource):
    def get(self):
        # get data
        X = get_data(2)
        # get predection
        predictions = SVCM_model.predict(X)
        # return predected events percent
        return count(predictions)

# Artificial neural network
class NNM (Resource):
    def get(self):
        # get data
        X = get_data(2)
        # get predection
        predictions = NNM_model.predict_classes(X)
        # return predected events percent
        return count(predictions)

# Recurrent neural network
class RNN (Resource):
    def get(self):
        # get data
        X = get_data(2)
        # Reformat dataset
        X = createWindows(X)
        # get predection
        predictions = RNM_model.predict_classes(X)
        # return predected events percent
        return count(predictions)

# start class   
class start (Resource):
    def get(self):
        print ("hi mmh")
        return "welcome to our server please choose wich directio you want (add ( /rfm , /lrm , /sgdc , /svc , /nnm ,/rnn ) to your link )"

# add apis (creat links)
api.add_resource(RFM, '/rfm') # link to Random Forest model
api.add_resource(LRM, '/lrm') # link to Logistic regression model
api.add_resource(SGDC,'/sgdc') # link to Stochastic gradient descent model
api.add_resource(SVC, '/svc') # link to Support vector machine model
api.add_resource(NNM, '/nnm') # link to Artificial neural network model
api.add_resource(RNN, '/rnn') # link to Artificial neural network model
api.add_resource(start, '/') # link to start

# run server
if __name__ == '__main__':
    app.run(debug=True)