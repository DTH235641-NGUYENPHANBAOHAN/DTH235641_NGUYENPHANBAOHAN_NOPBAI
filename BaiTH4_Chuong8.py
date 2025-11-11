import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Máy tính bỏ túi")
root.geometry("300x400")

entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5, relief="sunken", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

expression = ""

def button_click(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
        expression = ""
        entry.delete(0, tk.END)

def button_clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('Clr',5,0)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                  command=button_equal).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'Clr':
        tk.Button(root, text=text, width=25, height=2, font=('Arial', 12),
                  command=button_clear).grid(row=row, column=col, columnspan=4, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()