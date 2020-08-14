from mpu9250_i2c import *
from datetime import datetime
from firebase import firebase
import time
import sys
import os
time.sleep(1) # delay necessary to allow mpu9250 to settle
firebase= firebase.FirebaseApplication('https://drive-behaviour.firebaseio.com/')
file = open("Data.csv", "a")
if os.stat("Data.csv").st_size == 0:
        file.write("Data,Time,UptimeNanos,\
_1X_Acelerometro,_1Y_Acelerometro,_1Z_Acelerometro,\
_2X_Giroscope,_2Y_Giroscope,_2Z_Giroscope\n")
try:
    while True:
        ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
        now = datetime.now()
        d = now.strftime("%d/%m/%Y")
        t = now.strftime("%H:%M:%S")
        nano = time.time_ns()
        ############################################# Print Data in screen
        print('{}'.format('-'*30))
        print('accel [g]:  x = {}, y = {}, z = {}'.format(ax,ay,az))
        print('gyro [dps]: x = {}, y = {}, z = {}'.format(wx,wy,wz))
        print('{}'.format('-'*30))
        ############################################# Send Data to Server
        firebase.post('DriveBehaviour', 
                      {'Data':str(d),'Time':str(t),'UptimeNanos':str(nano),
                       '_1X_Acelerometro':str(ax),'_1Y_Acelerometro':str(ay),'_1Z_Acelerometro':str(az),
                       '_2X_Giroscope':str(wx),'_2Y_Giroscope':str(wy),'_2Z_Giroscope':str(wz)})
        ############################################# Save Data to File
        file.write(str(d)+","+str(t)+","+str(nano) \
               +","+str(ax)+","+str(ay)+","+str(az) \
               +","+str(wx)+","+str(wy)+","+str(wz)+"\n")
        file.flush()
        time.sleep(0.1)
    file.close()
except KeyboardInterrupt:
    sys.exit()