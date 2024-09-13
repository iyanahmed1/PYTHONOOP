import tkinter as tk

def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(value))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Error')

def theme_selector(theme):
    if theme == 'dark':
        root.configure(bg='#000000')
        display.configure(bg='#555555', fg='#ffffff')
        button_frame.configure(bg='#333333')  # Update button frame background
        for button in button_list:
            button.configure(bg='#444444', fg='#ffffff')
    elif theme == 'light':
        root.configure(bg='#ffffff')
        display.configure(bg='#e0e0e0', fg='#000000')
        button_frame.configure(bg='#cccccc')  # Update button frame background
        for button in button_list:
            button.configure(bg='#dddddd', fg='#000000')
    else:
        print('Invalid theme selected. Please choose between "light" or "dark".')

def handle_keypress(event):
    key = event.char
    if key in '0123456789':
        button_click(key)
    elif key in '+-*/':
        button_click(key)
    elif key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace key
        clear_display()
    elif key == 'c' or key == 'C':
        clear_display()

def set_theme_to_light():
    theme_selector('light')

def set_theme_to_dark():
    theme_selector('dark')

# Create the main window
root = tk.Tk()
root.title('Calculator')
root.geometry('400x500')
root.resizable(False, False)
root.configure(bg='#ADD8E6')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add a "Theme" menu
theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Light", command=set_theme_to_light)
theme_menu.add_command(label="Dark", command=set_theme_to_dark)

display = tk.Entry(root, font=('Arial', 24), borderwidth=5, relief='flat', justify='right')
display.pack(pady=20, padx=20, fill='both')

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

row = 0
col = 0

button_list = []  # List to keep track of button references

for button in buttons:
    action = lambda x=button: button_click(x) if x != '=' and x != 'C' else calculate() if x == '=' else clear_display()
    btn = tk.Button(button_frame, text=button, width=9, height=3, bg='#79E5F2', command=action)
    btn.grid(row=row, column=col, padx=5, pady=5)
    button_list.append(btn)  # Add button reference to list
    col += 1
    if col > 3:
        col = 0
        row += 1

root.bind('<Key>', handle_keypress)

root.mainloop()
