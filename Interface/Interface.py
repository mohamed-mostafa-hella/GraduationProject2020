#inport libraries 
from tkinter import *
from tkinter import ttk
import requests

#######################################################
#variables
names = ["Aggressive Right Curve",
         "Aggressive Left Curve",
         "Non Aggressive",
         "Aggressive Exchange Lane",
         "Aggressive Braking",
         "Aggressive Acceleration",
         "Rate",
         "Evaluation"]

nmodels=['Random Forest',
         'Logistic regression',
         'Stochastic gradient descent',
         'Support vector machine','Neural network',
         'Recurrent neural network']


models = [ 'rfm' , 'lrm' , 'sgdc' , 'svc' , 'nnm','rnn']
Rates=["Dangerous","Bad",'Not Bad',"Good","Perfect"]
########################################################
# function reques data from API and return result in 2_D array
def get_Y(index):
    link = 'http://127.0.0.1:5000/' 
    model=models[index]
    result = requests.get(link+model)
    result.status_code
    result =result.json()
    model_out = [] 
    for i in result:
        #t = int(float(i))
        #print(names[t-1]," = ",result[i])
        model_out.append(result[i])
    return model_out

#######################################################
#funcation to get Rate
def getRate(arr):
    #rate= 50-2*arr[0]-3*arr[1]+2*arr[2]-1*arr[3]-4*arr[4]-2*arr[5]
    rate= (((-1*(arr[0]+arr[1]+arr[3]+arr[4]+arr[5])) + 4*arr[2])+100)/500*100
    if rate<35:
        return Rates[0],rate
    if rate<50:
        return Rates[1],rate
    if rate<65:
        return Rates[2],rate
    if rate<85:
        return Rates[3],rate
    return Rates[4],rate

#######################################################
# function append result to Table(tree_view)
def Load():    
    data = get_Y(Box.current())
    evaluation,rate=getRate(data)
    data.append(rate)
    data.append(evaluation)
    for i in range(0,8):
        table.set(i,0,data[i]) 
            
########################################################
def createTable():
    table=ttk.Treeview(root,height=8)
    table.heading('#0', text='Event')
    for i in range(0,len(names)):
        table.insert('', i,i,text=names[i])
    table.config(column=('model'))
    table.heading( 0, text='Result')
    table.column(0, anchor='center')
    table.pack()
    return table           
            
            
# design interface
root=Tk(className=' Driver Behavior ') # frame (parent)
root['bg']='#457B9D'
root.geometry('500x300')
root.resizable(0, 0)

##Style
style=ttk.Style()
style.configure("TCombobox", padding=8, relief="flat",foreground='#1D3557' )
style.configure('TButton', relief="raised",font = ('Arial', 16 , 'normal'), borderwidth = '0',foreground='#457B9D') 
style.map('TButton', foreground = [('active', '#1D3557')],  background = [('active', 'Black')]) 
style.configure("Treeview.Heading", font=('Arial', 12))
style.configure("Treeview", font=('Arial', 10))


                                    
                                    
Box=ttk.Combobox(root,values=nmodels)
Box.current(4)
Box.pack()

table=createTable()


# create buttom
photo = PhotoImage(file = "loading.png")
photo=photo.subsample(18,18)
Bload=ttk.Button(root,text="Load Result",image=photo,compound=RIGHT)
Bload.pack() # show buttom on the parent


# listener to buttom click
Bload.config(command=Load)

# pause system running
root.mainloop()




