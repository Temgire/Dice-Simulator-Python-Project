# Project : Dice Simulator
# Author : Dinesh Temgire


import random
from tkinter import *

root=Tk()
root.geometry("700x450")

l1=Label(root,font=("times",200))

def roll():
    number=['\u2680','\u2861','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1=Button(root,text="lets roll...",command=roll)
b1.place(x=325,y=40)

l2=Label(root,text="Author : Dinesh Temgire")
l2.place(x=450,y=0)

root.mainloop()



