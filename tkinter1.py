#we import tkinter
import tkinter as tk  

#creating a window
window = tk.Tk()

#set the geometry
window.geometry('500x500')
#we set the title
window.title('My first Window')

# a label
label=tk.Label(window,text='Hello World!', font=('Arial',18))#window is the parent
 #to get the label into the window
label.pack(padx=20,pady=20) 

#a textbox
textbox=tk.Text(window,height=2,font=('Arial',16))#usually the user inputs the text
textbox.pack(padx=10)
#an entry i a textbox with height 1 without multi line features
#myentry=tk.Entry(window, font=('Arial',14))
#myentry.pack()

#adding a grid
buttonframe=tk.Frame(window)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

#we use buttonframe as the parent because the buttonframe is inside the window
#while the buuton is going to be inside the buttonframe
button1=tk.Button(buttonframe,text='1',font=('Arial',18))
button1.grid(row=0, column=0, sticky=tk.W + tk.E)#we dont use th pack function. sticky= makes the widget stick to side of the grid cell placed

button2=tk.Button(buttonframe,text='2',font=('Arial',18))
button2.grid(row=0, column=1, sticky=tk.W + tk.E)
 
button3=tk.Button(buttonframe,text='3',font=('Arial',18))
button3.grid(row=0, column=2, sticky=tk.W + tk.E)

button4=tk.Button(buttonframe,text='4',font=('Arial',18))
button4.grid(row=1, column=0, sticky=tk.W + tk.E)

button5=tk.Button(buttonframe,text='5',font=('Arial',18))
button5.grid(row=1, column=1, sticky=tk.W + tk.E)

button6=tk.Button(buttonframe,text='6',font=('Arial',18))
button6.grid(row=1, column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill='x')#means its going to strech into the x demensions



#add a button
button=tk.Button(window, text='Click Here', font=('Arial',14))
button.pack(pady=10)


#we call the constructor
window.mainloop()