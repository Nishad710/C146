# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:19:35 2021

@author: Nishad Ranjan 
"""
from tkinter import *
root = Tk()
root.title("Fibonacci Sum")
root.geometry("400x400")
 
label_series = Label(root,text="Fibonacci Series: ")
label_flower = Label(root,text = "Fibonacci Sum: ")
entry = Entry(root)
    
def Fibonaccisum():
  num = int(entry.get())
  first_no = 0
  second_no = 1
  sum = 0
  sum1 = 0
  counter = 1
  while (counter <= num):
    label_series["text"]+=str(sum) + "" 
    label_flower["text"] = "Fibonacci Sum: " + str(sum1)
    counter = counter + 1
    first_no = second_no
    second_no = sum
    sum = first_no + second_no
    sum1 = sum1 + sum
btn = Button(root,text="Show Fibonacci Series",command=Fibonaccisum)
entry.pack()
btn.pack()
label_series.pack()
label_flower.pack()
root.mainloop()
