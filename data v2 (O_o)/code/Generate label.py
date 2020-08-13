import pandas as pd
import numpy as np
folders=['new 16','new 17','new 20','new 21']
sensors=['NEW_giroscopio_terra.csv','NEW_acelerometro_terra.csv']
classes=np.array(pd.read_excel('class.xlsx'))

for folder in folders:
    gro=np.array(pd.read_csv(folder+'\groundTruth.csv'))
    for sensor in sensors:
        sheet =pd.read_csv(folder+'\\' +sensor)
        result=[]
        for sample in np.array(sheet):
            time=sample[9]
            State=False
            for record in gro:               
                if time>=record[1] and time<=record[2]:                    
                    State=True
                    for clas in classes:
                        if clas[0]==record[0]:
                            key=clas[1]
                            if key==7:
                                key=4
                            result.append(key)
                            break
                continue
            if State==False:
                result.append(0)
        sheet['Time']=sheet['vps']
        sheet=sheet.drop(columns=['time','ctime','vps','val','timestamp','uptimeNanos'])
        sheet['Lebal']=result
        sheet.to_csv(folder+' labeled ' +sensor)
