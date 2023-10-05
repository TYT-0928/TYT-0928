import tkinter as tk
from tkinter import *
from random import randint as ri
import math

ws = Tk()
ws.title("終極密碼")
ws.geometry('380x200')
ws['bg'] = '#ffbf00'
set_number = ri(1,100) #從1到100的整數隨機挑一個數字
min_value = 1
max_value = 100

gamer_input_number = '輸入1-100的整數'
txt = tk.StringVar()
txt.set(gamer_input_number)


def button_event():
    try:
        num = int(input_number.get())
        global set_number,min_value,max_value,gamer_input_number
        while num > 100 or num < 1: #不可讓使用者輸入小於1或大於100的整數
            gamer_input_number = '請遵守遊戲規則\n 請輸入1-100以內的整數'
            txt.set(gamer_input_number)
            break
        while 1< num < 100:
            if num > set_number:
                max_value = num
                gamer_input_number = f'猜的數字太大了，請輸入{min_value}-{max_value}的整數'    
            elif num < set_number:
                min_value = num
                gamer_input_number = f'猜的數字太小了，請輸入{min_value}-{max_value}的整數'     
            else:
                gamer_input_number = f'猜對了~答案就是{set_number}唷~~'
            txt.set(gamer_input_number)
            break
    except: #若玩家輸入文字或小數就會執行這段程式碼並跳出提示訊息
        if isinstance(input_number.get(),str):
            gamer_input_number = f'勿輸入文字或小數\n 請輸入{min_value}-{max_value}的整數'
        # else:
        #     gamer_input_number = f'請遵守遊戲規則\n 請輸入{min_value}-{max_value}的整數'
        txt.set(gamer_input_number)
    
# 設定提示訊息的位置、字體大小
Label(ws, textvariable=txt, pady=2, font=('Comic Sans MS',15)).pack()

# 設定使用者輸入數字的位置
input_number = Entry(ws)
input_number.place(x=120,y=125)

# enter鈕的位置
Button(
    ws,
    text="Enter", 
    padx=10, 
    pady=3,
    command=button_event
    ).pack()

ws.mainloop()
