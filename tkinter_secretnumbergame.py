import tkinter as tk
from tkinter import *
from random import randint as ri
import math

ws = Tk()
ws.title("終極密碼")
ws.geometry('380x200')
ws['bg'] = '#ffbf00'
set_number = ri(1,100)
min_value = 1
max_value = 100

str = '輸入1-100的整數'
txt = tk.StringVar()
txt.set(str)

def button_event():
    num = int(input_number.get())
    global set_number,min_value,max_value,str
    while num > 100 or num < 1:
        str = '請遵守遊戲規則\n 請輸入1-100以內的整數'
        txt.set(str)
        break
    while 1< num < 100:
        if num > set_number:
            max_value = num
            str = f'猜的數字太大了，請輸入{min_value}-{max_value}的整數'    
        elif num < set_number:
            min_value = num
            str = f'猜的數字太小了，請輸入{min_value}-{max_value}的整數'     
        else:
            str = f'猜對了~答案就是{set_number}唷~~'
        txt.set(str)
        break
    
Label(ws, textvariable=txt, pady=2, font=('Comic Sans MS',13)).pack()

input_number = Entry(ws)
input_number.place(x=120,y=125)


Button(
    ws,
    text="Enter", 
    padx=10, 
    pady=3,
    command=button_event
    ).pack()

ws.mainloop()