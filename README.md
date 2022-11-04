
# Driver Behavior Based on Deep Learning

Driver behaviors have a lot of effects in many fields. The bad driver has a negative impact on safety for the human soul if this person was another drive or a passer. Also, in the economy. The bad driver damages cars or buses. and he reduces its life span Which means a lot of cost for the Maintenance and the replacement. and for The environment, destroyed cars and its parts are a big problem for its recycling or at least Get rid of it. Our idea aims to measure driver behavior based on artificial intelligence (AI), to provide a fair rating for companies to track drivers'behaviors to save human souls and preserve the life of their car. This leads to preserving the environment.



## Driver Rate
![Rating](https://github.com/mohamed-mostafa-hella/GraduationProject2020/blob/master/images/rating.png?raw=true)
## OBJECTIVES

The general objective is to help drivers to develop their skills to save 
humans life, reduce the cost for companies and rescue the environment 
from rubbish.

#### specific objectives 
    - Provide a fair rate for driver behavior to help companies to choose the 
        best driver for their services.

    - Provide a Full report to help the driver at the Development process by 
        learning from his mistakes at The previous trip.

    - Provide more than one model for analysis and prediction.

    - Provide API to use this system with different types of Applications.

## MATRERIALS& MODELS

To collect data We need sensors and CPU with OS. And this may be the 
device's meaning.

#### The tracking device
    - sensors:-
        - IMU Sensor (MPU-9250) figure 1.1
    - Mini PC:-
        - Raspberry Pi figure 1.2
    - power source:-
        - Power Bank figure 1.3
    - Wires:-
        - JUMPERS figure 1.4
![MATRERIALS& MODELS](https://github.com/mohamed-mostafa-hella/GraduationProject2020/blob/master/images/componant.png?raw=true)

#### Data Uploading

we used firebase to receive data from Raspberry Pi and 
store it before pass it to API.

![firebase logo](https://firebase.google.com/images/social.png)


#### AI Model:

We built several models to try to gain a lot of accuracies and choose the 
best model which is stable for problem-solving.

- Our Models
    - Machine Learning
        - Random Forest
        - Logistic Regression
        - Stochastic Gradient Descent
        - Support Vector Machine
    - Deep learning
        - Artificial Neural Network
        - Recurrent Neural Network

#### Application Programming Interface (API):

By flask we gained the ability to build a local server to load data from 
firebase and process it by selected model and return the result as a JSON 
file.

Our API run on a local server but, at last days we succeeded to provide an 
online host and our API is available to use widely.

![firebase logo](data:image/png;base64,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)

#### Graphical user interface (GUI):

Python with Tkinter library was a good partner to build an interface 
provide to the user to select the model and to load report (result)

![firebase logo](https://github.com/mohamed-mostafa-hella/GraduationProject2020/blob/master/images/dfd.png?raw=true) DFD Level 1

#### Data Backup

During a time of data collection and uploading, we had to avoid any 
failure like connection lost or reach the limit of storage on firebase or any 
damage may happen for data during pass it to API so, we did it in two 
ways.

Offline backup: save a copy of data in sheet at Raspberry Pi storage
Online backup: make a copy from data on firebase and store it at Google 
Drive.


## RESULTS

The user loads the result as a table from Two columns The first for Title 
’Event’ and The second for Value ‘Result’.

![RESULTS](https://github.com/mohamed-mostafa-hella/GraduationProject2020/blob/master/images/tables.png?raw=true)


- The rows from 1:6 are returned from API. every row act as one class 
    and its value is the ratio for the event by the total time of the trip.

- Row no7 ‘Rate’ is calculated from all the above values by a simple 
    equation.
    - Y=(-(e1+e2+e4+e5+e6)+4xe3+100)/500

- Raw no8 ‘Evaluation’ is dependent on Y value it is calculated by 
    conditions.

    - Dangerous
        - Less than 35%
    - Bad
        - 35 : 50%
    - Not Bad
        - 50: 65%
    - Good
        - 65: 85%
    - Perfect
        - Greater than 85%

The user could choose between 5 models available now to classify driver 
behavior during the trip.

#### This model is:-

- Random Forest
- Logistic regression
- Stochastic gradient descent
- Support vector machine
- Neural network
- Recurrent neural network

The default model is Artificial Neural Network.
## CONCLUSION

At the end of documentation and the project finally, we can monitor
driver behavior.

From this project, we can collect the sensor data then upload it to the
Database and analysis this data, then the company can make decisions
based on our output.


## REFERENCES

1- [https://github.com/jair-jr/driverBehaviorDataset](https://github.com/jair-jr/driverBehaviorDataset)

2- [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.017495
9](https://github.com/jair-jr/driverBehaviorDataset)

3- [https://www.tensorflow.org/guide](https://www.tensorflow.org/guide)

4- [https://flask.palletsprojects.com/en/1.1.x/api/](https://flask.palletsprojects.com/en/1.1.x/api/)

5- [https://machinelearningmastery.com](https://machinelearningmastery.com)

6- [https://www.kaggle.com](https://www.kaggle.com)

7- [https://www.youtube.com/channel/UCxxljM6JkSvJVSD_T90ZnMw](https://www.youtube.com/channel/UCxxljM6JkSvJVSD_T90ZnMw)

8- [https://www.wikipedia.org](https://www.wikipedia.org)

9- [https://firebase.google.com/docs/database](https://firebase.google.com/docs/database)

10- [https://www.raspberrypi.org/forums/](https://www.raspberrypi.org/forums/)
## ACKNOWLEDGEMENT

It has been a great opportunity to gain lots of experience in real-time 
projects, followed by the knowledge of how to actually design and 
analyse real projects. For that, we want to thank all the people who made 
it possible for students like us. Special thanks to the graduation project 
unit for the efforts they did to provide us with all useful information and 
making the path clear for the students to implement all the education 
periods in real-time project design and analysis. Furthermore, we all the 
professors and visiting industry for the interesting lectures they presented 
which had great benefit for all of us. We would like to express our 
deepest gratitude to our graduation project supervisor Dr. Fatma sakr for 
his patience and guidance throughout the semester.
## TEAM MEMBERS

- [@Mohamed Mosad](https://github.com/Mohamed-Mosad)
- [@Mohamed Shaban](https://github.com/Ghazidan1)
- [@Mohamed Mostafa](https://github.com/mohamed-mostafa-hella)
- [@Mohamed Samir](https://github.com/Mohamed-Mosad)
- [@Aya Sobhy](https://github.com/ayasobhyy)
- [@Shrouk Nabil](https://github.com/ShroukNabil)
