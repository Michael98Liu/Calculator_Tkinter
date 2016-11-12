# __Author__: Fengyuan Michael Liu
# __E-mail: liufengyuan1998@hotmail.com
# __Time__: 12, Nov., 2016
# __Description: A GUI calculator written in python using tkinter

import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()

result = StringVar()
result.set('0')
tempresult = 0

def shownum(num): # Show input numbers as a string
    try:
        if int(result.get()) == 0:
            result.set(num)
        else:
            result.set(result.get() + num)
    except:
        result.set(result.get() + num)

def delete_one():
    result.set(result.get()[:-1])
    if result.get() == '':
        result.set('0')

def delete_all():
    result.set('0')

def calculate(sign, tempresult):
    previoussign = ''
    ispresign = False
    # To decide if it's the first number
    for i in result.get()[1:]:
        if i == '+' or i == '-' or i == '*' or i == '/':
            ispresign = True
            previoussign = i
    if ispresign:
        if previoussign == '+':
            temp = result.get().split('+')
            # To see if the first number is a negative
            try:
                tempresult = float(temp[0]) + float(temp[1])
            except:
                tempresult = 0 - float(temp[0][1:])  + float(temp[1])
        elif previoussign == '-':
            temp = result.get().split('-')
            try:
                tempresult = float(temp[0]) - float(temp[1])
            except:
                tempresult = 0 - float(temp[1]) - float(temp[2])
        elif previoussign == '/':
            temp = result.get().split('/')
            try:
                tempresult = float(temp[0]) / float(temp[1])
            except:
                tempresult = (0 - float(temp[0][1:])) / float(temp[1])
        elif previoussign == '*':
            temp = result.get().split('*')
            try:
                tempresult = float(temp[0]) * float(temp[1])
            except:
                tempresult = (0 - float(temp[0][1:])) * float(temp[1])
        if sign == '=':
            result.set(str(tempresult))
        else:
            result.set(str(tempresult) + sign)
    else:
        if sign == '=':
            result.set(str(tempresult))
        else:
            result.set(result.get() + sign)


# Divide window into two seperate frames for display and buttons respectively
windowframe = ttk.Frame(root)
windowframe.pack()
window = ttk.Label(windowframe, textvariable = result, anchor = 'w', justify = RIGHT, font = ('Courier', 18, 'bold'))
window.pack(anchor = 'e')
buttons = ttk.Frame(root)
buttons.pack()

# Add buttons to the frame
deleteall = tk.Button(buttons, text = 'C', width = 6, height = 3, command = delete_all)
deleteall.grid(row = 0, column = 0)
deleteone = tk.Button(buttons, text = 'Del', width = 6, height = 3, command = delete_one)
deleteone.grid(row = 0, column = 1)
divide = tk.Button(buttons, text = '/', width = 6, height = 3, command = lambda: calculate('/', tempresult))
divide.grid(row = 0, column = 2)
multiply = tk.Button(buttons, text = '*', width = 6, height = 3, command = lambda: calculate('*', tempresult))
multiply.grid(row = 0, column = 3)
seven = tk.Button(buttons, text = '7', width = 6, height = 3, command = lambda: shownum('7'))
seven.grid(row = 1, column = 0)
eight = tk.Button(buttons, text = '8', width = 6, height = 3, command = lambda: shownum('8'))
eight.grid(row = 1, column = 1)
nine = tk.Button(buttons, text = '9', width = 6, height = 3, command = lambda: shownum('9'))
nine.grid(row = 1, column = 2)
minus = tk.Button(buttons, text = '-', width = 6, height = 3, command = lambda: calculate('-', tempresult))
minus.grid(row = 1, column = 3)
four = tk.Button(buttons, text = '4', width = 6, height = 3, command = lambda: shownum('4'))
four.grid(row = 2, column = 0)
five = tk.Button(buttons, text = '5', width = 6, height = 3, command = lambda: shownum('5'))
five.grid(row = 2, column = 1)
six = tk.Button(buttons, text = '6', width = 6, height = 3, command = lambda: shownum('6'))
six.grid(row = 2, column = 2)
plus = tk.Button(buttons, text = '+', width = 6, height = 3, command = lambda: calculate('+', tempresult))
plus.grid(row = 2, column = 3)
one = tk.Button(buttons, text = '1', width = 6, height = 3, command = lambda: shownum('1'))
one.grid(row = 3, column = 0)
two = tk.Button(buttons, text = '2', width = 6, height = 3, command = lambda: shownum('2'))
two.grid(row = 3, column = 1)
one = tk.Button(buttons, text = '3', width = 6, height = 3, command = lambda: shownum('3'))
one.grid(row = 3, column = 2)
zero = tk.Button(buttons, text = '0', width = 13, height = 3, command = lambda: shownum('0'))
zero.grid(row = 4, column = 0, columnspan = 2)
dot = tk.Button(buttons, text = '.', width = 6, height = 3, command = lambda: shownum('.'))
dot.grid(row = 4, column = 2)
equal = tk.Button(buttons, text = '=', width = 6, height = 7, command = lambda: calculate('=', tempresult))
equal.grid(row = 3, column = 3, rowspan = 2)


root.mainloop()
