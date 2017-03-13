from __future__ import division
from Tkinter import *

main = Tk()
main.title("Calculator")
main.geometry("375x550")

entry = Text(main)
entry.configure(width=17,height=1)
entry.place(x=13, y=5)
entry.config(font=("Courier", 25))

def oneButtonFunction(event):
    entry.insert(END, '1')
def twoButtonFunction(event):
    entry.insert(END, '2')
def threeButtonFunction(event):
    entry.insert(END, '3')
def fourButtonFunction(event):
    entry.insert(END, '4')
def fiveButtonFunction(event):
    entry.insert(END, '5')
def sixButtonFunction(event):
    entry.insert(END, '6')
def sevenButtonFunction(event):
    entry.insert(END, '7')
def eightButtonFunction(event):
    entry.insert(END, '8')
def nineButtonFunction(event):
    entry.insert(END, '9')
def zeroButtonFunction(event):
    entry.insert(END, '0')
def addButtonFunction(event):
    entry.insert(END, '+')
def subButtonFunction(event):
    entry.insert(END, '-')
def multButtonFunction(event):
    entry.insert(END, '*')
def divButtonFunction(event):
    entry.insert(END, '/')
def decimalButtonFunction(event):
    entry.insert(END, '.')
def equalButtonFunction(event):
    x = entry.get("1.0", "end-1c")
    entry.delete("1.0", END)
    entry.insert(END, eval(x))
def clearButtonFunction(event):
    entry.delete("1.0", END)
def parentheses1ButtonFuction(event):
    entry.insert(END, '(')
def parentheses2ButtonFuction(event):
    entry.insert(END, ')')
def trigButtonFunction(event):
    pass

oneButton = Button(main, text="1", width=10, height=5)
oneButton.place(x=10, y=50)
oneButton.bind('<Button-1>', oneButtonFunction)

twoButton = Button(main, text="2", width=10, height=5)
twoButton.place(x=100, y=50)
twoButton.bind('<Button-1>', twoButtonFunction)

threeButton = Button(main, text="3", width=10, height=5)
threeButton.place(x=190, y=50)
threeButton.bind('<Button-1>', threeButtonFunction)

fourButton = Button(main, text="4", width=10, height=5)
fourButton.place(x=10, y=150)
fourButton.bind('<Button-1>', fourButtonFunction)

fiveButton = Button(main, text="5", width=10, height=5)
fiveButton.place(x=100, y=150)
fiveButton.bind('<Button-1>', fiveButtonFunction)

sixButton = Button(main, text="6", width=10, height=5)
sixButton.place(x=190, y=150)
sixButton.bind('<Button-1>', sixButtonFunction)

sevenButton = Button(main, text="7", width=10, height=5)
sevenButton.place(x=10, y=250)
sevenButton.bind('<Button-1>', sevenButtonFunction)

eightButton = Button(main, text="8", width=10, height=5)
eightButton.place(x=100, y=250)
eightButton.bind('<Button-1>', eightButtonFunction)

nineButton = Button(main, text="9", width=10, height=5)
nineButton.place(x=190, y=250)
nineButton.bind('<Button-1>', nineButtonFunction)

zeroButton = Button(main, text="0", width=10, height=5)
zeroButton.place(x=100, y=350)
zeroButton.bind('<Button-1>', zeroButtonFunction)

decimalButton = Button(main, text=".", width=10, height=5)
decimalButton.place(x=10, y=350)
decimalButton.bind('<Button-1>', decimalButtonFunction)

equalButton = Button(main, text="=", width=10, height=5)
equalButton.place(x=190, y=350)
equalButton.bind('<Button-1>', equalButtonFunction)

addButton = Button(main, text="+", width=10, height=5)
addButton.place(x=280, y=50)
addButton.bind('<Button-1>', addButtonFunction)

subButton = Button(main, text="-", width=10, height=5)
subButton.place(x=280, y=150)
subButton.bind('<Button-1>', subButtonFunction)

multButton = Button(main, text="X", width=10, height=5)
multButton.place(x=280, y=250)
multButton.bind('<Button-1>', multButtonFunction)

divButton = Button(main, text="/", width=10, height=5)
divButton.place(x=280, y=350)
divButton.bind('<Button-1>', divButtonFunction)

clearButton = Button(main, text="Clear", width=10, height=5)
clearButton.place(x=10, y=450)
clearButton.bind('<Button-1>', clearButtonFunction)

parentheses1Button = Button(main, text="(", width=10, height=5)
parentheses1Button.place(x=100, y=450)
parentheses1Button.bind('<Button-1>', parentheses1ButtonFuction)

parentheses2Button = Button(main, text=")", width=10, height=5)
parentheses2Button.place(x=190, y=450)
parentheses2Button.bind('<Button-1>', parentheses2ButtonFuction)

trigButton = Button(main, text="Trig", width=10, height=5)
trigButton.place(x=280, y=450)
trigButton.bind('<Button-1>', trigButtonFunction)




main.mainloop()
