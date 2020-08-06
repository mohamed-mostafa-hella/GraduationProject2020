from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import joblib
from firebase import firebase
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)
api = Api(app)

model = joblib.load('finalized_model.sav')
firebase = firebase.FirebaseApplication('https://drive-behaviour.firebaseio.com/',None)

# parser = reqparse.RequestParser()
# parser.add_argument('query')

class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        #args = parser.parse_args()
        #user_query = args['query']
        # vectorize the user's query and make a prediction
        ##uq_vectorized = model.vectorizer_transform(
            ##np.array([user_query]))

        result = firebase.get('/DriveBehaviour',None)
        
        X_data = []
        for key in result:
            X_data.append([result [key]['_1X_Acelerometro'] ,
                  result [key]['_1Y_Acelerometro'] ,
                  result [key]['_1Z_Acelerometro'] ,
                  result [key]['_2X_Giroscope'] ,
                  result [key]['_2Y_Giroscope'] ,
                  result [key]['_2Z_Giroscope']])
        X_data = np.array(X_data)
        poly = PolynomialFeatures(degree=2 , include_bias=False)
        X=poly.fit_transform(X_data)

        predictions = model.predict(X)


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
        
        return counter

class start (Resource):
    def get(self):
        return "welcome to our server blease choose wich directio you want (add (/ai) to your link )"

api.add_resource(PredictSentiment, '/ai')
api.add_resource(start, '/')

if __name__ == '__main__':
    app.run(debug=True)