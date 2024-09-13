import tkinter as tk
root= tk.Tk()
root.geometry('500x400')
text_results=tk.Text(root,height=2, width=16, font=('Arial',24))
text_results.grid(columnspan=5)
root.mainloop()