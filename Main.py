from tkinter import *
from tkinter import ttk

def show_message():
    label['text'] = entry.get()
    
def on_button_click(value):
    # добавляем значение кнопки в строку ввода
    current_text = entry.get()
    entry.delete(0, END)
    entry.insert(0, current_text + str(value))
    
def calculate(value):
    result = eval(value)
    entry.delete(0,END)
    entry.insert(0,str(result))

root = Tk()
root.title('calculate')
root.geometry('550x450')


entry = ttk.Entry(root)
entry.grid(row=0, column=0, columnspan=4, ipadx=140, ipady=8, padx=8, pady=8)


btn1 = ttk.Button(root, text="1", command=lambda: on_button_click(1))
btn1.grid(row=4, column=2, ipadx=25, ipady=5, padx=4, pady=4)

btn2 = ttk.Button(root, text="2", command=lambda: on_button_click(2))
btn2.grid(row=4, column=1, ipadx=25, ipady=5, padx=4, pady=4)

btn3 = ttk.Button(root, text="3", command=lambda: on_button_click(3))
btn3.grid(row=4, column=0, ipadx=25, ipady=5, padx=4, pady=4)

btn4 = ttk.Button(root, text="4", command=lambda: on_button_click(4))
btn4.grid(row=3, column=2, ipadx=25, ipady=5, padx=4, pady=4)

btn5 = ttk.Button(root, text="5", command=lambda: on_button_click(5))
btn5.grid(row=3, column=1, ipadx=25, ipady=5, padx=4, pady=4)

btn6 = ttk.Button(root, text="6", command=lambda: on_button_click(6))
btn6.grid(row=3, column=0, ipadx=25, ipady=5, padx=4, pady=4)

btn7 = ttk.Button(root, text="7", command=lambda: on_button_click(7))
btn7.grid(row=2, column=2, ipadx=25, ipady=5, padx=4, pady=4)

btn8 = ttk.Button(root, text="8", command=lambda: on_button_click(8))
btn8.grid(row=2, column=1, ipadx=25, ipady=5, padx=4, pady=4)

btn9 = ttk.Button(root, text="9", command=lambda: on_button_click(9))
btn9.grid(row=2, column=0, ipadx=25, ipady=5, padx=4, pady=4)

btn0 = ttk.Button(root, text="0", command=lambda: on_button_click(0))
btn0.grid(row=5, column=1, ipadx=25, ipady=5, padx=4, pady=4)

btn_result = ttk.Button(root, text="=", command=lambda: calculate(entry.get()))
btn_result.grid(row=5, column=2, ipadx=25, ipady=5, padx=4, pady=4)

btn_delete = ttk.Button(root, text="Delete", command=lambda: entry.delete(0,END))
btn_delete.grid(row=5, column=0, ipadx=25, ipady=5, padx=4, pady=4)

btn_plus = ttk.Button(root, text="+", command=lambda: on_button_click('+'))
btn_plus.grid(row=2, column=3, ipadx=25, ipady=5, padx=4, pady=4)

btn_minus = ttk.Button(root,text="-",command=lambda: on_button_click("-"))
btn_minus.grid(row=3, column=3, ipadx=25, ipady=5, padx=5, pady=4,)

btn_multiply = ttk.Button(root, text="*", command=lambda: on_button_click("*"))
btn_multiply.grid(row=4, column=3, ipadx=25, ipady=5, padx=5, pady=4)

btn_divide = ttk.Button(root, text="/", command=lambda: on_button_click("/"))
btn_divide.grid(row=5, column=3, ipadx=25, ipady=5, padx=5, pady=4)

root.mainloop()
