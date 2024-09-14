import tkinter as tk

class MyGUI:
    def __init__(self):
        self.root=tk.Tk()
        self.label=tk.Label(self.root, text='Your message', font=('Arial',18))
        self.label.pack(padx=10, pady=10)

        self.textbox=tk.Text(self.root, height= 5, font=('Arial',16))
        self.textbox.pack(padx=10, pady=10, )

        self.check_state=tk.IntVar()#hold integer values for various widget operations
        self.check=tk.Checkbutton(self.root, text='Show Message box' ,font=('Arial',20), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button=tk.Button(self.root, text='Show Message', font=('Arial',18), command=self.show_message)
        # command ensure that the function is excuted when the button is clicked,
        #  no parentheses because we are passing show message and not calling it
        self.button.pack(padx=10,pady=10 )

        self.root.mainloop()

    #adding functionality
    def show_message(self):
        if self.check_state.get()==0:
            print(self.textbox.)

MyGUI()
