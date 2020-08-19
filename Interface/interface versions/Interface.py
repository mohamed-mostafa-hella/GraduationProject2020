#inport libraries 
from tkinter import *
from tkinter import ttk
import random
import requests

#######################################################
#variables
names = ["aggressive right curve",
         "aggressive left turn",
         "event_nao_aggressive",
         "exchange aggressive right lane",
         "aggressive braking",
         "aggressive acceleration"]

models = [ 'rfm' , 'lrm' , 'sgdc' , 'svc' , 'nnm']
########################################################
# function reques data from API and return result in 2_D array
def get_Y():
    link = 'http://127.0.0.1:5000/' 
    out=[]
    for model in models:
        result = requests.get(link+model)
        result.status_code
        result =result.json()

        model_out = [] 
        for i in result:
            t = int(float(i))
            #print(names[t-1]," = ",result[i])
            model_out.append(result[i])

        out.append(model_out)
        
    return out
#######################################################
# function append result to Table(tree_view)
def Load():    
    data = get_Y()
    for i in range(0,6):
        for j in range(0,5):
            table.set(i,j,data[j][i]) 
            
########################################################
# design interface
root=Tk() # frame (parent)
table=ttk.Treeview(root,height=6) # tree_view (table)
table.pack() # show tree_view on the parent
table.heading('#0', text='Event') # first colum
#insert event name to first colum
for i in range(0,6):
    table.insert('', i,i,text=names[i])
    
#creat table (creat colums)
table.config(column=('RFM','LRM','SGDC','SVC','NNM'))
table.heading('#1', text='Random Forest')
table.heading('#2', text='Logistic regression')
table.heading('#3', text='Stochastic gradient descent')
table.heading('#4', text='Support vector machine')
table.heading('#5', text='Neural network')

# create buttom
Bload=Button(root,text="Load Result")
Bload.pack() # show buttom on the parent

# add value text in the center of the cell
for c in range(0,5):
    table.column(c, anchor='center')

# listener to buttom click
Bload.config(command=Load)

# pause system running
root.mainloop()




